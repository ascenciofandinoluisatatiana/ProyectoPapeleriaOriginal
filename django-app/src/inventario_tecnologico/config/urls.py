from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Imports para Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Inventario SENA",
        default_version='v1',
        description="""
        API REST para el Sistema de Inventario Tecnológico SENA.

        Esta API proporciona endpoints para:
        - Gestión de activos (CRUD completo)
        - Consulta de categorías y ubicaciones
        - Estadísticas y reportes
        - Logs de auditoría
        """,
        terms_of_service="https://www.sena.edu.co/terminos/",
        contact=openapi.Contact(email="inventario@sena.edu.co"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventario.urls')),

    # Documentación de la API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)