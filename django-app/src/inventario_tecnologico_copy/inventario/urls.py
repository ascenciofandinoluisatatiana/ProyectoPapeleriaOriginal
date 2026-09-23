"""
URLs para la aplicación de inventario.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api

app_name = 'inventario'

# =========================================
# ROUTER DE LA API REST
# =========================================

router = DefaultRouter()

# Registrar ViewSets
router.register(r'activos', api.ActivoViewSet, basename='activo-api')
router.register(r'categorias', api.CategoriaViewSet, basename='categoria-api')
router.register(r'ubicaciones', api.UbicacionViewSet, basename='ubicacion-api')
router.register(r'estados', api.EstadoViewSet, basename='estado-api')
router.register(r'logs', api.LogViewSet, basename='log-api')

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Activos - CRUD completo
    path('activos/', views.ActivoListView.as_view(), name='activo_list'),
    path('activos/crear/', views.ActivoCreateView.as_view(), name='activo_create'),
    path('activos/<int:pk>/', views.ActivoDetailView.as_view(), name='activo_detail'),
    path('activos/<int:pk>/editar/', views.ActivoUpdateView.as_view(), name='activo_update'),
    path('activos/<int:pk>/eliminar/', views.ActivoDeleteView.as_view(), name='activo_delete'),
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/crear/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),
    # URLs de autenticación
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('registro/', views.registro_usuario, name='registro'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('cambiar-password/', views.CambiarPasswordView.as_view(), name='cambiar_password'),
    path('logs/', views.LogListView.as_view(), name='log_list'),
    path('logs/<int:pk>/', views.LogDetailView.as_view(), name='log_detail'),

    # Categorías
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),

    # Ubicaciones
    path('ubicaciones/', views.UbicacionListView.as_view(), name='ubicacion_list'),

    # Reportes
    path('reportes/inventario-pdf/', views.reporte_inventario_pdf, name='reporte_inventario_pdf'),
    path('reportes/ubicaciones-pdf/', views.reporte_ubicaciones_pdf, name='reporte_ubicaciones_pdf'),
    path('exportar/activos-excel/', views.exportar_activos_excel_view, name='exportar_activos_excel'),
    path('exportar/logs-excel/', views.exportar_logs_excel_view, name='exportar_logs_excel'),

    # =========================================
    # API REST (agregado al final)
    # =========================================
    path('api/', include(router.urls)),
]
