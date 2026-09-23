from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Ubicacion, Estado, Activo, HistorialMovimiento, Mantenimiento
from .models import Activo, Perfil, Log  # <-- asegúrate que Perfil esté aquí

class CategoriaAdmin(admin.ModelAdmin):
    """
    Configuración del modelo Categoría en el panel administrativo.
    """
    
    list_display = (
        'codigo',
        'nombre',
        'mostrar_estado',
        'fecha_creacion',
        'fecha_modificacion'
    )
    
    search_fields = (
        'nombre',
        'codigo',
        'descripcion'
    )
    
    list_filter = (
        'activa',
        'fecha_creacion',
        'fecha_modificacion'
    )
    
    readonly_fields = (
        'fecha_creacion',
        'fecha_modificacion'
    )
    
    ordering = ('nombre',)
    
    list_per_page = 20
    
    fields = (
        'nombre',
        'codigo',
        'descripcion',
        'activa',
        'fecha_creacion',
        'fecha_modificacion'
    )
    
    def mostrar_estado(self, obj):
        """Muestra el estado de la categoría con un badge de color."""
        if obj.activa:
            color = '#28a745'
            texto = 'ACTIVA'
        else:
            color = '#dc3545'
            texto = 'INACTIVA'
        
        return format_html(
            '<span style="background-color: {}; color: white; '
            'padding: 5px 10px; border-radius: 3px; '
            'font-weight: bold; font-size: 11px; '
            'display: inline-block;">'
            '{}'
            '</span>',
            color,
            texto
        )
    
    mostrar_estado.short_description = 'Estado'
    mostrar_estado.admin_order_field = 'activa'
    
    def activar_categorias(self, request, queryset):
        """Acción para activar las categorías seleccionadas."""
        actualizadas = queryset.update(activa=True)
        mensaje = f'{actualizadas} categoría(s) activada(s) exitosamente.'
        self.message_user(request, mensaje)
    
    activar_categorias.short_description = 'Activar categorías seleccionadas'
    
    def desactivar_categorias(self, request, queryset):
        """Acción para desactivar las categorías seleccionadas."""
        actualizadas = queryset.update(activa=False)
        mensaje = f'{actualizadas} categoría(s) desactivada(s) exitosamente.'
        self.message_user(request, mensaje)
    
    desactivar_categorias.short_description = 'Desactivar categorías seleccionadas'
    
    actions = [activar_categorias, desactivar_categorias]


admin.site.register(Categoria, CategoriaAdmin)

class UbicacionAdmin(admin.ModelAdmin):
    """Configuración del admin para Ubicaciones."""

    list_display = (
        'codigo',
        'nombre',
        'tipo',
        'capacidad',
        'responsable',
        'mostrar_estado'
    )

    search_fields = (
        'nombre',
        'codigo',
        'responsable'
    )

    list_filter = (
        'tipo',
        'activa',
        'fecha_creacion'
    )

    readonly_fields = (
        'fecha_creacion',
        'fecha_modificacion'
    )

    ordering = ('nombre',)

    list_per_page = 20

    fields = (
        'nombre',
        'tipo',
        'codigo',
        'capacidad',
        'responsable',
        'observaciones',
        'activa',
        'fecha_creacion',
        'fecha_modificacion'
    )

    def mostrar_estado(self, obj):
        """Badge de estado."""
        if obj.activa:
            color = '#28a745'
            texto = 'ACTIVA'
        else:
            color = '#dc3545'
            texto = 'INACTIVA'

        return format_html(
            '<span style="background-color: {}; color: white; '
            'padding: 5px 10px; border-radius: 3px; '
            'font-weight: bold; font-size: 11px;">'
            '{}'
            '</span>',
            color,
            texto
        )

    mostrar_estado.short_description = 'Estado'
    mostrar_estado.admin_order_field = 'activa'


# Registrar el modelo
admin.site.register(Ubicacion, UbicacionAdmin)




class EstadoAdmin(admin.ModelAdmin):
    list_display = (
        'orden',
        'codigo',
        'nombre',
        'mostrar_color',
        'es_operativo',
        'requiere_accion',
        'mostrar_estado'
    )

    search_fields = ('nombre', 'codigo')
    list_filter = ('es_operativo', 'requiere_accion', 'activo')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    ordering = ('orden', 'nombre')

    def mostrar_color(self, obj):
        return format_html(
            '<span style="background-color: {}; color: white; '
            'padding: 5px 15px; border-radius: 3px;">'
            '{}</span>',
            obj.color, obj.color
        )
    mostrar_color.short_description = 'Color'

    def mostrar_estado(self, obj):
        color = '#28a745' if obj.activo else '#dc3545'
        texto = 'ACTIVO' if obj.activo else 'INACTIVO'
        return format_html(
            '<span style="background: {}; color: white; '
            'padding: 5px 10px; border-radius: 3px;">{}</span>',
            color, texto
        )
    mostrar_estado.short_description = 'Estado'


admin.site.register(Estado, EstadoAdmin)



class ActivoAdmin(admin.ModelAdmin):
    """Configuración del admin para Activos."""

    list_display = (
        'codigo_inventario',
        'nombre',
        'categoria',
        'ubicacion',
        'estado',
        'marca',
        'mostrar_valor',
        'mostrar_estado_sistema'
    )

    list_filter = (
        'categoria',
        'ubicacion',
        'estado',
        'activo'
    )

    search_fields = (
        'codigo_inventario',
        'nombre',
        'numero_serie',
        'marca'
    )

    readonly_fields = (
        'fecha_creacion',
        'fecha_modificacion',
        'mostrar_foto_preview'
    )

    fieldsets = (
        ('Información Básica', {
            'fields': (
                'codigo_inventario',
                'nombre',
                'descripcion',
                'categoria'
            )
        }),
        ('Relaciones', {
            'fields': ('ubicacion', 'estado')
        }),
        ('Detalles del Producto', {
            'fields': ('marca', 'modelo', 'numero_serie')
        }),
        ('Financiero', {
            'fields': ('fecha_adquisicion', 'valor_adquisicion')
        }),
        ('Gestión', {
            'fields': ('responsable', 'observaciones')
        }),
        ('Multimedia', {
            'fields': ('foto', 'mostrar_foto_preview')
        }),
        ('Control', {
            'fields': ('activo', 'fecha_creacion', 'fecha_modificacion'),
            'classes': ('collapse',)
        })
    )

    def mostrar_valor(self, obj):
        if obj.valor_adquisicion:
            return f"${obj.valor_adquisicion:,.0f}"
        return "-"
    mostrar_valor.short_description = 'Valor'

    def mostrar_estado_sistema(self, obj):
        color = '#28a745' if obj.activo else '#dc3545'
        texto = 'ACTIVO' if obj.activo else 'INACTIVO'
        return format_html(
            '<span style="background: {}; color: white; '
            'padding: 5px 10px; border-radius: 3px;">{}</span>',
            color, texto
        )
    mostrar_estado_sistema.short_description = 'Estado'

    def mostrar_foto_preview(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" style="max-width: 300px; '
                'border-radius: 8px;" />',
                obj.foto.url
            )
        return "Sin fotografía"
    mostrar_foto_preview.short_description = 'Vista Previa'


admin.site.register(Activo, ActivoAdmin)


class HistorialMovimientoAdmin(admin.ModelAdmin):
    list_display = (
        'activo',
        'ubicacion_origen',
        'ubicacion_destino',
        'motivo',
        'usuario',
        'fecha_movimiento',
        'aprobado'
    )
    list_filter = ('motivo', 'aprobado', 'fecha_movimiento')
    search_fields = ('activo__codigo_inventario', 'usuario')
    readonly_fields = ('fecha_movimiento',)
    ordering = ('-fecha_movimiento',)


admin.site.register(HistorialMovimiento, HistorialMovimientoAdmin)


class MantenimientoAdmin(admin.ModelAdmin):
    list_display = (
        'activo',
        'tipo',
        'fecha_inicio',
        'fecha_fin',
        'tecnico',
        'mostrar_costo',
        'estado_mantenimiento'
    )
    list_filter = ('tipo', 'estado_mantenimiento')
    search_fields = ('activo__codigo_inventario', 'tecnico')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    ordering = ('-fecha_inicio',)

    def mostrar_costo(self, obj):
        return obj.get_costo_formateado()
    mostrar_costo.short_description = 'Costo'


admin.site.register(Mantenimiento, MantenimientoAdmin)


"""
=========================================
ADMIN PERFIL DE USUARIO
=========================================
"""

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class PerfilInline(admin.StackedInline):
    """Inline para mostrar perfil en el admin de User."""
    model = Perfil
    can_delete = False
    verbose_name = 'Perfil'
    verbose_name_plural = 'Perfiles'
    
    fieldsets = (
        ('Información Laboral', {
            'fields': ('cargo', 'departamento', 'telefono')
        }),
        ('Multimedia', {
            'fields': ('foto',)
        }),
    )


class UserAdmin(BaseUserAdmin):
    """Admin personalizado para User con Perfil inline."""
    inlines = (PerfilInline,)


# Re-registrar UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['fecha_hora', 'usuario_nombre', 'accion', 'modelo', 'objeto_repr', 'ip_address']
    list_filter = ['accion', 'modelo', 'fecha_hora']
    search_fields = ['usuario_nombre', 'descripcion', 'objeto_repr']
    readonly_fields = [
        'usuario', 'usuario_nombre', 'accion', 'modelo', 'objeto_id',
        'objeto_repr', 'fecha_hora', 'descripcion', 'datos_anteriores',
        'datos_nuevos', 'ip_address', 'user_agent'
    ]
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False