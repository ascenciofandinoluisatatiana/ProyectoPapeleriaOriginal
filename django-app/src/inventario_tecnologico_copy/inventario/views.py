import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum, Count, Q, Avg
from .models import Activo, Categoria, Ubicacion, Estado, HistorialMovimiento, Mantenimiento, Log
from .forms import ActivoForm, CategoriaForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegistroForm, LoginForm, PerfilForm, UserForm
from .utils.pdf_generator import generar_reporte_inventario_general, generar_reporte_activos_por_ubicacion
from .utils.excel_generator import exportar_activos_excel, exportar_logs_excel


@login_required
def dashboard(request):
    """Panel principal con estadísticas generales del inventario."""
    total_activos = Activo.objects.filter(activo=True).count()
    total_categorias = Categoria.objects.filter(activa=True).count()
    total_ubicaciones = Ubicacion.objects.filter(activa=True).count()

    valor_total = Activo.objects.filter(activo=True).aggregate(
        total=Sum('valor_adquisicion')
    )['total'] or 0

    activos_por_estado = Estado.objects.annotate(
        cantidad=Count('activos')
    ).order_by('orden')

    top_categorias = Categoria.objects.filter(activa=True).annotate(
        cantidad_activos=Count('activos', filter=Q(activos__activo=True))
    ).order_by('-cantidad_activos')[:5]

    ultimos_movimientos = HistorialMovimiento.objects.select_related(
        'activo', 'ubicacion_origen', 'ubicacion_destino'
    ).order_by('-fecha_movimiento')[:5]

    actividad_reciente = Log.objects.select_related('usuario').order_by('-fecha_hora')[:10]

    mantenimientos_pendientes = Mantenimiento.objects.select_related(
        'activo'
    ).filter(
        estado_mantenimiento__in=['PENDIENTE', 'EN_PROCESO']
    ).order_by('fecha_inicio')[:5]

    context = {
        'total_activos': total_activos,
        'total_categorias': total_categorias,
        'total_ubicaciones': total_ubicaciones,
        'valor_total': valor_total,
        'actividad_reciente': actividad_reciente,
        'activos_por_estado': activos_por_estado,
        'top_categorias': top_categorias,
        'ultimos_movimientos': ultimos_movimientos,
        'mantenimientos_pendientes': mantenimientos_pendientes,
    }
    return render(request, 'inventario/dashboard.html', context)


class ActivoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Listado de activos con búsqueda, filtros y paginación."""
    model = Activo
    template_name = 'inventario/activo_list.html'
    context_object_name = 'activos'
    permission_required = 'inventario.view_activo'
    paginate_by = 20

    def get_queryset(self):
        queryset = Activo.objects.select_related(
            'categoria', 'ubicacion', 'estado'
        ).filter(activo=True)

        search = self.request.GET.get('search')
        categoria_id = self.request.GET.get('categoria')
        estado_id = self.request.GET.get('estado')

        if search:
            queryset = queryset.filter(
                Q(codigo_inventario__icontains=search) |
                Q(nombre__icontains=search) |
                Q(marca__icontains=search)
            )

        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)

        if estado_id:
            queryset = queryset.filter(estado_id=estado_id)

        return queryset.order_by('-fecha_creacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.filter(activa=True)
        context['estados'] = Estado.objects.filter(activo=True)
        context['search'] = self.request.GET.get('search', '')
        context['categoria_seleccionada'] = self.request.GET.get('categoria', '')
        context['estado_seleccionado'] = self.request.GET.get('estado', '')
        return context


class ActivoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Detalle de un activo: información completa, historial y mantenimientos."""
    model = Activo
    template_name = 'inventario/activo_detail.html'
    context_object_name = 'activo'
    permission_required = 'inventario.view_activo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movimientos'] = self.object.historial_movimientos.select_related(
            'ubicacion_origen', 'ubicacion_destino'
        ).order_by('-fecha_movimiento')
        context['mantenimientos'] = self.object.mantenimientos.order_by('-fecha_inicio')
        return context


class CategoriaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Listado de categorías con conteo de activos."""
    model = Categoria
    template_name = 'inventario/categoria_list.html'
    context_object_name = 'categorias'
    permission_required = 'inventario.view_categoria'

    def get_queryset(self):
        return Categoria.objects.filter(activa=True).annotate(
            cantidad_activos=Count('activos', filter=Q(activos__activo=True))
        ).order_by('nombre')


class UbicacionListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Listado de ubicaciones con conteo de activos."""
    model = Ubicacion
    template_name = 'inventario/ubicacion_list.html'
    context_object_name = 'ubicaciones'
    permission_required = 'inventario.view_ubicacion'

    def get_queryset(self):
        return Ubicacion.objects.filter(activa=True).annotate(
            cantidad_activos=Count('activos', filter=Q(activos__activo=True))
        ).order_by('nombre')


# ========================================
# VISTAS CRUD DE ACTIVOS
# ========================================

class ActivoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Vista para crear nuevos activos."""
    model = Activo
    form_class = ActivoForm
    template_name = 'inventario/activo_form.html'
    success_url = reverse_lazy('inventario:activo_list')
    permission_required = 'inventario.add_activo'

    def form_valid(self, form):
        response = super().form_valid(form)

        Log.registrar(
            usuario=self.request.user,
            accion='CREATE',
            modelo='Activo',
            objeto=self.object,
            descripcion=f'Creó el activo {self.object.codigo_inventario}',
            datos_nuevos={
                'codigo': self.object.codigo_inventario,
                'descripcion': self.object.descripcion,
                'categoria': str(self.object.categoria),
                'ubicacion': str(self.object.ubicacion),
                'estado': str(self.object.estado),
                'valor_adquisicion': float(self.object.valor_adquisicion) if self.object.valor_adquisicion else 0,
            },
            request=self.request
        )

        messages.success(self.request, f'✓ Activo {self.object.codigo_inventario} creado exitosamente.')
        return response


class ActivoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Vista para editar activos."""
    model = Activo
    form_class = ActivoForm
    template_name = 'inventario/activo_form.html'
    permission_required = 'inventario.change_activo'

    def get_success_url(self):
        return reverse_lazy('inventario:activo_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Guardar estado ANTES
        datos_anteriores = {
            'codigo': self.object.codigo_inventario,
            'descripcion': self.object.descripcion,
            'categoria': str(self.object.categoria),
            'ubicacion': str(self.object.ubicacion),
            'estado': str(self.object.estado),
            'valor_adquisicion': float(self.object.valor_adquisicion) if self.object.valor_adquisicion else 0,
        }

        response = super().form_valid(form)

        # Guardar estado DESPUÉS
        self.object.refresh_from_db()
        datos_nuevos = {
            'codigo': self.object.codigo_inventario,
            'descripcion': self.object.descripcion,
            'categoria': str(self.object.categoria),
            'ubicacion': str(self.object.ubicacion),
            'estado': str(self.object.estado),
            'valor_adquisicion': float(self.object.valor_adquisicion) if self.object.valor_adquisicion else 0,
        }

        # Detectar cambios
        cambios = []
        for key in datos_anteriores:
            if datos_anteriores[key] != datos_nuevos[key]:
                cambios.append(f"{key}: {datos_anteriores[key]} → {datos_nuevos[key]}")

        Log.registrar(
            usuario=self.request.user,
            accion='UPDATE',
            modelo='Activo',
            objeto=self.object,
            descripcion=f'Actualizó {self.object.codigo_inventario}. Cambios: {", ".join(cambios) if cambios else "Sin cambios"}',
            datos_anteriores=datos_anteriores,
            datos_nuevos=datos_nuevos,
            request=self.request
        )

        messages.success(self.request, f'✓ Activo {self.object.codigo_inventario} actualizado.')
        return response


class ActivoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Vista para eliminar activos."""
    model = Activo
    template_name = 'inventario/activo_confirm_delete.html'
    success_url = reverse_lazy('inventario:activo_list')
    permission_required = 'inventario.delete_activo'

    def form_valid(self, form):
        self.object = self.get_object()

        # Guardar datos ANTES de eliminar
        datos_eliminados = {
            'codigo': self.object.codigo_inventario,
            'descripcion': self.object.descripcion,
            'categoria': str(self.object.categoria),
            'ubicacion': str(self.object.ubicacion),
            'estado': str(self.object.estado),
            'valor_adquisicion': float(self.object.valor_adquisicion) if self.object.valor_adquisicion else 0,
        }

        # Registrar ANTES de eliminar
        Log.registrar(
            usuario=self.request.user,
            accion='DELETE',
            modelo='Activo',
            objeto=self.object,
            descripcion=f'Eliminó el activo {self.object.codigo_inventario}',
            datos_anteriores=datos_eliminados,
            request=self.request
        )

        messages.warning(self.request, f'⚠ Activo {self.object.codigo_inventario} eliminado.')
        return super().form_valid(form)


class CategoriaCreateView(CreateView):
    """Vista para crear una nueva categoría."""
    model = Categoria
    form_class = CategoriaForm
    template_name = 'inventario/categoria_form.html'
    success_url = reverse_lazy('inventario:categoria_list')

    def form_valid(self, form):
        messages.success(
            self.request,
            f'Categoría "{form.instance.nombre}" creada exitosamente.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Error al crear la categoría. Por favor revise los campos marcados.'
        )
        return super().form_invalid(form)


class CategoriaUpdateView(UpdateView):
    """Vista para editar una categoría existente."""
    model = Categoria
    form_class = CategoriaForm
    template_name = 'inventario/categoria_form.html'
    success_url = reverse_lazy('inventario:categoria_list')

    def form_valid(self, form):
        messages.success(
            self.request,
            f'Categoría "{form.instance.nombre}" actualizada exitosamente.'
        )
        return super().form_valid(form)


class CategoriaDeleteView(DeleteView):
    """Vista para eliminar una categoría."""
    model = Categoria
    template_name = 'inventario/categoria_confirm_delete.html'
    success_url = reverse_lazy('inventario:categoria_list')

    def delete(self, request, *args, **kwargs):
        categoria = self.get_object()
        messages.success(
            request,
            f'Categoría "{categoria.nombre}" eliminada exitosamente.'
        )
        return super().delete(request, *args, **kwargs)


"""
=========================================
VISTAS DE AUTENTICACIÓN
=========================================
"""

def registro_usuario(request):
    """Vista para registrar nuevos usuarios."""
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            Log.registrar(
                usuario=user,
                accion='CREATE',
                modelo='User',
                descripcion=f'Nuevo usuario registrado: {user.username}',
                request=request
            )
            # Login automático después del registro
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.username}! Tu cuenta ha sido creada.')
            return redirect('inventario:dashboard')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = RegistroForm()

    return render(request, 'inventario/registro.html', {'form': form})


def login_usuario(request):
    """Vista para login de usuarios."""
    if request.user.is_authenticated:
        return redirect('inventario:dashboard')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                Log.registrar(
                    usuario=user,
                    accion='LOGIN',
                    modelo='User',
                    descripcion=f'Inició sesión en el sistema',
                    request=request
                )

                messages.success(request, f'¡Bienvenido {user.username}!')

                # Redirigir a la página que intentaba acceder
                next_url = request.GET.get('next', 'inventario:dashboard')
                return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'inventario/login.html', {'form': form})


@login_required
def logout_usuario(request):
    """Vista para cerrar sesión."""
    Log.registrar(
        usuario=request.user,
        accion='LOGOUT',
        modelo='User',
        descripcion=f'Cerró sesión',
        request=request
    )
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('inventario:login')

@login_required
def perfil_usuario(request):
    """Vista para ver y editar el perfil del usuario."""
    perfil = request.user.perfil

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            Log.registrar(
                usuario=request.user,
                accion='UPDATE',
                modelo='Perfil',
                descripcion='Actualizó su perfil',
                request=request
            )
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('inventario:perfil')
    else:
        user_form = UserForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)

    context = {
        'user_form': user_form,
        'perfil_form': perfil_form,
    }
    return render(request, 'inventario/perfil.html', context)


class CambiarPasswordView(LoginRequiredMixin, PasswordChangeView):
    """Vista para cambiar contraseña."""
    form_class = PasswordChangeForm
    template_name = 'inventario/cambiar_password.html'
    success_url = reverse_lazy('inventario:perfil')

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña cambiada correctamente.')
        return super().form_valid(form)


"""
=========================================
VISTAS DE AUDITORÍA
=========================================
"""


class LogListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Vista para listar logs de auditoría."""
    model = Log
    template_name = 'inventario/log_list.html'
    context_object_name = 'logs'
    paginate_by = 50
    permission_required = 'inventario.view_log'

    def get_queryset(self):
        queryset = Log.objects.all().select_related('usuario')

        usuario = self.request.GET.get('usuario')
        if usuario:
            queryset = queryset.filter(usuario_nombre__icontains=usuario)

        accion = self.request.GET.get('accion')
        if accion:
            queryset = queryset.filter(accion=accion)

        modelo = self.request.GET.get('modelo')
        if modelo:
            queryset = queryset.filter(modelo=modelo)

        fecha_desde = self.request.GET.get('fecha_desde')
        if fecha_desde:
            queryset = queryset.filter(fecha_hora__date__gte=fecha_desde)

        fecha_hasta = self.request.GET.get('fecha_hasta')
        if fecha_hasta:
            queryset = queryset.filter(fecha_hora__date__lte=fecha_hasta)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro_usuario'] = self.request.GET.get('usuario', '')
        context['filtro_accion'] = self.request.GET.get('accion', '')
        context['filtro_modelo'] = self.request.GET.get('modelo', '')
        context['filtro_fecha_desde'] = self.request.GET.get('fecha_desde', '')
        context['filtro_fecha_hasta'] = self.request.GET.get('fecha_hasta', '')
        context['acciones'] = Log.ACCIONES
        context['modelos'] = Log.objects.values_list('modelo', flat=True).distinct()
        return context


class LogDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Vista para ver detalle de un log."""
    model = Log
    template_name = 'inventario/log_detail.html'
    context_object_name = 'log'
    permission_required = 'inventario.view_log'



# ========================================
# VISTAS PARA REPORTES PDF Y EXCEL
# ========================================

@login_required
@permission_required('inventario.view_activo', raise_exception=True)
def reporte_inventario_pdf(request):
    """Generar reporte PDF de inventario general."""
    try:
        activos = Activo.objects.filter(activo=True).select_related(
            'categoria', 'ubicacion', 'estado'
        )

        pdf_path = generar_reporte_inventario_general(activos)

        Log.registrar(
            usuario=request.user,
            accion='EXPORT',
            modelo='Activo',
            descripcion='Generó reporte PDF de inventario general',
            request=request
        )

        return FileResponse(
            open(pdf_path, 'rb'),
            content_type='application/pdf',
            as_attachment=True,
            filename=os.path.basename(pdf_path)
        )

    except Exception as e:
        messages.error(request, f'Error al generar reporte: {str(e)}')
        return redirect('inventario:activo_list')


@login_required
@permission_required('inventario.view_activo', raise_exception=True)
def reporte_ubicaciones_pdf(request):
    """Generar reporte PDF de activos agrupados por ubicación."""
    try:
        activos = Activo.objects.filter(activo=True).select_related(
            'categoria', 'ubicacion', 'estado'
        )

        pdf_path = generar_reporte_activos_por_ubicacion(activos)

        Log.registrar(
            usuario=request.user,
            accion='EXPORT',
            modelo='Activo',
            descripcion='Generó reporte PDF de activos por ubicación',
            request=request
        )

        return FileResponse(
            open(pdf_path, 'rb'),
            content_type='application/pdf',
            as_attachment=True,
            filename=os.path.basename(pdf_path)
        )

    except Exception as e:
        messages.error(request, f'Error al generar reporte: {str(e)}')
        return redirect('inventario:activo_list')


@login_required
@permission_required('inventario.view_activo', raise_exception=True)
def exportar_activos_excel_view(request):
    """Exportar listado de activos a Excel."""
    try:
        activos = Activo.objects.filter(activo=True).select_related(
            'categoria', 'ubicacion', 'estado'
        )

        excel_path = exportar_activos_excel(activos)

        Log.registrar(
            usuario=request.user,
            accion='EXPORT',
            modelo='Activo',
            descripcion='Exportó activos a Excel',
            request=request
        )

        return FileResponse(
            open(excel_path, 'rb'),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            filename=os.path.basename(excel_path)
        )

    except Exception as e:
        messages.error(request, f'Error al exportar: {str(e)}')
        return redirect('inventario:activo_list')


@login_required
@permission_required('inventario.view_log', raise_exception=True)
def exportar_logs_excel_view(request):
    """Exportar logs de auditoría a Excel."""
    try:
        logs = Log.objects.all().select_related('usuario').order_by('-fecha_hora')

        excel_path = exportar_logs_excel(logs)

        Log.registrar(
            usuario=request.user,
            accion='EXPORT',
            modelo='Log',
            descripcion='Exportó logs de auditoría a Excel',
            request=request
        )

        return FileResponse(
            open(excel_path, 'rb'),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            filename=os.path.basename(excel_path)
        )

    except Exception as e:
        messages.error(request, f'Error al exportar: {str(e)}')
        return redirect('inventario:log_list')