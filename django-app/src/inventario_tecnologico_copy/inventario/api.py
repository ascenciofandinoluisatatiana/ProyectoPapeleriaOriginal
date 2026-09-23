"""
Vistas de la API REST para el sistema de inventario.

Este módulo contiene todos los ViewSets que manejan
los endpoints de la API.

ViewSets incluidos:
- CategoriaViewSet: CRUD completo de categorías
- UbicacionViewSet: CRUD completo de ubicaciones
- EstadoViewSet: Solo lectura de estados
- ActivoViewSet: CRUD completo de activos + endpoints personalizados
- LogViewSet: Solo lectura de logs de auditoría
"""

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Count, Sum, Q, Avg, Max, Min
from django.utils import timezone
from datetime import timedelta

from .models import (
    Activo,
    Categoria,
    Ubicacion,
    Estado,
    Log
)

from .serializers import (
    ActivoListSerializer,
    ActivoDetailSerializer,
    CategoriaSerializer,
    UbicacionSerializer,
    EstadoSerializer,
    LogSerializer,
    EstadisticasSerializer,
)


# =========================================
# VIEWSETS DE CATÁLOGOS
# =========================================

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de Categorías.

    Endpoints automáticos que proporciona:
    - GET    /api/categorias/       → Lista todas
    - POST   /api/categorias/       → Crea nueva
    - GET    /api/categorias/{id}/  → Detalle de una
    - PUT    /api/categorias/{id}/  → Actualiza completa
    - PATCH  /api/categorias/{id}/  → Actualiza parcial
    - DELETE /api/categorias/{id}/  → Elimina una

    Filtros disponibles:
    - Búsqueda: ?search=computo
    - Ordenamiento: ?ordering=nombre, ?ordering=-cantidad_activos
    """

    # QuerySet base con anotación de cantidad
    queryset = Categoria.objects.annotate(
        cantidad_activos=Count(
            'activos',
            filter=Q(activos__activo=True)
        )
    ).order_by('nombre')

    # Serializer a usar
    serializer_class = CategoriaSerializer

    # Permisos necesarios
    permission_classes = [permissions.IsAuthenticated]

    # Filtros y búsqueda
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['nombre', 'cantidad_activos']
    ordering = ['nombre']


class UbicacionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de Ubicaciones.

    Similar a CategoriaViewSet pero para ubicaciones.
    """

    queryset = Ubicacion.objects.annotate(
        cantidad_activos=Count(
            'activos',
            filter=Q(activos__activo=True)
        )
    ).order_by('nombre')

    serializer_class = UbicacionSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['nombre', 'cantidad_activos']
    ordering = ['nombre']


class EstadoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet de SOLO LECTURA para Estados.

    Endpoints disponibles:
    - GET /api/estados/       → Lista todos
    - GET /api/estados/{id}/  → Detalle de uno

    NO permite POST, PUT, PATCH, DELETE.
    Los estados son datos maestros que no se modifican desde la API.
    """

    queryset = Estado.objects.filter(activo=True).order_by('nombre')
    serializer_class = EstadoSerializer
    permission_classes = [permissions.IsAuthenticated]


# =========================================
# VIEWSET DE ACTIVOS (Completo)
# =========================================

class ActivoViewSet(viewsets.ModelViewSet):
    """
    ViewSet completo para Activos.

    Endpoints automáticos:
    - GET    /api/activos/       → Lista paginada
    - POST   /api/activos/       → Crear activo
    - GET    /api/activos/{id}/  → Ver un activo
    - PUT    /api/activos/{id}/  → Actualizar completo
    - PATCH  /api/activos/{id}/  → Actualizar parcial
    - DELETE /api/activos/{id}/  → Eliminar (soft delete)

    Endpoints personalizados:
    - GET /api/activos/estadisticas/     → Estadísticas generales
    - GET /api/activos/por_categoria/    → Activos por categoría
    - GET /api/activos/por_ubicacion/    → Activos por ubicación
    - GET /api/activos/por_estado/       → Activos por estado
    - GET /api/activos/valor_total/      → Valor total del inventario
    - GET /api/activos/recientes/        → Últimos 10 activos creados

    Filtros disponibles:
    - Por categoría: ?categoria=1
    - Por ubicación: ?ubicacion=2
    - Por estado: ?estado=1
    - Búsqueda: ?search=laptop
    - Ordenamiento: ?ordering=-valor_adquisicion
    - Combinados: ?categoria=1&search=laptop&ordering=-fecha_creacion
    """

    # QuerySet base (solo activos activos)
    queryset = Activo.objects.filter(
        activo=True
    ).select_related(
        'categoria',
        'ubicacion',
        'estado'
    ).order_by('-fecha_creacion')

    # Permisos
    permission_classes = [permissions.IsAuthenticated]

    # Filtros
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Campos por los que se puede filtrar
    filterset_fields = [
        'categoria',
        'ubicacion',
        'estado',
    ]

    # Campos en los que se puede buscar
    search_fields = [
        'codigo_inventario',
        'nombre',
        'marca',
        'modelo',
        'numero_serie',
        'responsable',
    ]

    # Campos por los que se puede ordenar
    ordering_fields = [
        'codigo_inventario',
        'nombre',
        'valor_adquisicion',
        'fecha_adquisicion',
        'fecha_creacion',
    ]

    # Ordenamiento por defecto
    ordering = ['-fecha_creacion']

    def get_serializer_class(self):
        """
        Retorna el serializer apropiado según la acción:

        - retrieve (GET /api/activos/5/): ActivoDetailSerializer (completo)
        - list, create, update (otros): ActivoListSerializer (resumido)

        Esto optimiza el tamaño de las respuestas.
        """
        if self.action == 'retrieve':
            return ActivoDetailSerializer
        return ActivoListSerializer

    # =========================================
    # ENDPOINTS PERSONALIZADOS
    # =========================================

    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        """
        Endpoint personalizado: GET /api/activos/estadisticas/

        Retorna estadísticas generales del sistema de inventario.

        Ejemplo de respuesta:
        {
            "total_activos": 150,
            "total_categorias": 8,
            "total_ubicaciones": 12,
            "valor_total": "1250000.00",
            "activos_por_categoria": [
                {"categoria__nombre": "Computadores", "cantidad": 45},
                {"categoria__nombre": "Mobiliario", "cantidad": 30},
                ...
            ],
            ...
        }
        """
        activos = Activo.objects.filter(activo=True)

        data = {
            'total_activos': activos.count(),
            'total_categorias': Categoria.objects.count(),
            'total_ubicaciones': Ubicacion.objects.count(),
            'valor_total': activos.aggregate(
                Sum('valor_adquisicion')
            )['valor_adquisicion__sum'] or 0,
            'activos_por_categoria': list(
                activos.values('categoria__nombre')
                .annotate(cantidad=Count('id'))
                .order_by('-cantidad')
            ),
            'activos_por_ubicacion': list(
                activos.values('ubicacion__nombre')
                .annotate(cantidad=Count('id'))
                .order_by('-cantidad')
            ),
            'activos_por_estado': list(
                activos.values('estado__nombre')
                .annotate(cantidad=Count('id'))
                .order_by('-cantidad')
            ),
        }

        serializer = EstadisticasSerializer(data)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def por_categoria(self, request):
        """
        Endpoint: GET /api/activos/por_categoria/

        Retorna activos agrupados por categoría con conteo.
        """
        categorias = Categoria.objects.annotate(
            cantidad=Count('activos', filter=Q(activos__activo=True)),
            valor_total=Sum(
                'activos__valor_adquisicion',
                filter=Q(activos__activo=True)
            )
        ).values('id', 'nombre', 'cantidad', 'valor_total').order_by('-cantidad')

        return Response(list(categorias))

    @action(detail=False, methods=['get'])
    def por_ubicacion(self, request):
        """
        Endpoint: GET /api/activos/por_ubicacion/

        Retorna activos agrupados por ubicación con conteo.
        """
        ubicaciones = Ubicacion.objects.annotate(
            cantidad=Count('activos', filter=Q(activos__activo=True)),
            valor_total=Sum(
                'activos__valor_adquisicion',
                filter=Q(activos__activo=True)
            )
        ).values('id', 'nombre', 'cantidad', 'valor_total').order_by('-cantidad')

        return Response(list(ubicaciones))

    @action(detail=False, methods=['get'])
    def valor_total(self, request):
        """
        Endpoint: GET /api/activos/valor_total/

        Retorna el valor total del inventario.
        """
        activos = Activo.objects.filter(activo=True)

        valor = activos.aggregate(
            total=Sum('valor_adquisicion'),
            promedio=Avg('valor_adquisicion'),
            maximo=Max('valor_adquisicion'),
            minimo=Min('valor_adquisicion')
        )

        return Response({
            'valor_total': valor['total'] or 0,
            'valor_promedio': valor['promedio'] or 0,
            'valor_maximo': valor['maximo'] or 0,
            'valor_minimo': valor['minimo'] or 0,
            'cantidad_activos': activos.count()
        })

    @action(detail=False, methods=['get'])
    def recientes(self, request):
        """
        Endpoint: GET /api/activos/recientes/

        Retorna los 10 activos creados más recientemente.
        """
        activos = self.get_queryset().order_by('-fecha_creacion')[:10]
        serializer = self.get_serializer(activos, many=True)
        return Response(serializer.data)


# =========================================
# VIEWSET DE LOGS (Solo lectura)
# =========================================

class LogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet de SOLO LECTURA para Logs de auditoría.

    Endpoints disponibles:
    - GET /api/logs/       → Lista paginada
    - GET /api/logs/{id}/  → Detalle de un log

    NO permite POST, PUT, PATCH, DELETE.
    Los logs se crean automáticamente en el sistema,
    nunca desde la API.

    Filtros disponibles:
    - Por acción: ?accion=CREATE
    - Por modelo: ?modelo=Activo
    - Por usuario: ?usuario=1
    - Búsqueda: ?search=laptop
    - Ordenamiento: ?ordering=-fecha_hora
    """

    queryset = Log.objects.all().select_related(
        'usuario'
    ).order_by('-fecha_hora')

    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['accion', 'modelo', 'usuario']
    search_fields = ['usuario_nombre', 'descripcion', 'objeto_repr']
    ordering_fields = ['fecha_hora']
    ordering = ['-fecha_hora']