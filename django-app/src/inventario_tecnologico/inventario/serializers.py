"""
Serializers para la API REST del sistema de inventario.

Este módulo contiene todos los serializers que convierten
los modelos de Django a formato JSON y viceversa.

Serializers incluidos:
- CategoriaSerializer: Para el modelo Categoria
- UbicacionSerializer: Para el modelo Ubicacion
- EstadoSerializer: Para el modelo Estado
- ActivoListSerializer: Versión resumida de Activo
- ActivoDetailSerializer: Versión completa de Activo
- LogSerializer: Para logs de auditoría (solo lectura)
- EstadisticasSerializer: Para datos estadísticos agregados
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Activo,
    Categoria,
    Ubicacion,
    Estado,
    Log
)


# =========================================
# SERIALIZERS DE CATÁLOGOS (Categoría, Ubicación, Estado)
# =========================================

class CategoriaSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Categoria.

    Incluye un campo calculado 'cantidad_activos' que cuenta
    cuántos activos activos tiene cada categoría.
    Este campo se calcula en la vista usando annotate().
    """

    # Campo adicional calculado (viene de la vista con annotate)
    cantidad_activos = serializers.IntegerField(
        read_only=True,
        help_text="Cantidad de activos activos en esta categoría"
    )

    class Meta:
        model = Categoria
        fields = [
            'id',
            'nombre',
            'activa',
            'cantidad_activos',
        ]
        read_only_fields = ['id']


class UbicacionSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Ubicacion.

    Similar a CategoriaSerializer, incluye cantidad de activos.
    """

    cantidad_activos = serializers.IntegerField(
        read_only=True,
        help_text="Cantidad de activos activos en esta ubicación"
    )

    class Meta:
        model = Ubicacion
        fields = [
            'id',
            'nombre',
            'activa',
            'cantidad_activos',
        ]
        read_only_fields = ['id']


class EstadoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Estado.

    Serializer simple sin campos calculados adicionales.
    """

    class Meta:
        model = Estado
        fields = [
            'id',
            'nombre',
            'activo',
        ]
        read_only_fields = ['id']


# =========================================
# SERIALIZERS DE ACTIVOS
# =========================================

class ActivoListSerializer(serializers.ModelSerializer):
    """
    Serializer RESUMIDO para listas de activos.

    Este serializer se usa cuando se pide una LISTA de activos.
    No incluye todos los campos para que la respuesta sea más rápida.

    Campos adicionales:
    - categoria_nombre: Nombre legible de la categoría
    - ubicacion_nombre: Nombre legible de la ubicación
    - estado_nombre: Nombre legible del estado

    Uso: GET /api/activos/
    """

    # Campos de relaciones (nombres legibles)
    categoria_nombre = serializers.CharField(
        source='categoria.nombre',
        read_only=True,
        help_text="Nombre de la categoría"
    )

    ubicacion_nombre = serializers.CharField(
        source='ubicacion.nombre',
        read_only=True,
        help_text="Nombre de la ubicación"
    )

    estado_nombre = serializers.CharField(
        source='estado.nombre',
        read_only=True,
        help_text="Nombre del estado"
    )

    class Meta:
        model = Activo
        fields = [
            # Campos básicos
            'id',
            'codigo_inventario',
            'nombre',

            # IDs de relaciones (para editar)
            'categoria',
            'ubicacion',
            'estado',

            # Nombres de relaciones (para mostrar)
            'categoria_nombre',
            'ubicacion_nombre',
            'estado_nombre',

            # Datos importantes
            'valor_adquisicion',
            'fecha_adquisicion',
        ]


class ActivoDetailSerializer(serializers.ModelSerializer):
    """
    Serializer COMPLETO para detalle de un activo.

    Este serializer se usa cuando se pide UN activo específico.
    Incluye TODOS los campos y objetos completos de las relaciones.

    Campos adicionales:
    - categoria_detalle: Objeto completo de Categoria
    - ubicacion_detalle: Objeto completo de Ubicacion
    - estado_detalle: Objeto completo de Estado

    Uso: GET /api/activos/5/
    """

    # Objetos completos de las relaciones (nested)
    categoria_detalle = CategoriaSerializer(
        source='categoria',
        read_only=True,
        help_text="Objeto completo de la categoría"
    )

    ubicacion_detalle = UbicacionSerializer(
        source='ubicacion',
        read_only=True,
        help_text="Objeto completo de la ubicación"
    )

    estado_detalle = EstadoSerializer(
        source='estado',
        read_only=True,
        help_text="Objeto completo del estado"
    )

    class Meta:
        model = Activo
        fields = '__all__'  # TODOS los campos del modelo
        read_only_fields = [
            'id',
            'fecha_creacion',
            'fecha_modificacion',
        ]


# =========================================
# SERIALIZERS DE AUDITORÍA
# =========================================

class LogSerializer(serializers.ModelSerializer):
    """
    Serializer para logs de auditoría.

    Este serializer es de SOLO LECTURA. Los logs no se pueden
    crear, editar o eliminar desde la API.

    Campos adicionales:
    - usuario_nombre: Nombre del usuario que realizó la acción
    - accion_display: Nombre legible de la acción
    """

    # Campo calculado del nombre del usuario
    usuario_nombre = serializers.CharField(
        read_only=True,
        help_text="Nombre del usuario que realizó la acción"
    )

    # Nombre legible de la acción (en lugar del código)
    accion_display = serializers.CharField(
        source='get_accion_display',
        read_only=True,
        help_text="Acción en formato legible"
    )

    class Meta:
        model = Log
        fields = [
            'id',
            'usuario',
            'usuario_nombre',
            'accion',
            'accion_display',
            'modelo',
            'objeto_id',
            'objeto_repr',
            'descripcion',
            'fecha_hora',
            'ip_address',
            'user_agent',
        ]
        # TODOS los campos son solo lectura
        read_only_fields = fields


# =========================================
# SERIALIZERS DE DATOS AGREGADOS
# =========================================

class EstadisticasSerializer(serializers.Serializer):
    """
    Serializer para datos estadísticos.

    Este serializer NO está vinculado a un modelo.
    Se usa solo para estructurar datos calculados.

    Uso: Endpoint /api/activos/estadisticas/
    """

    # Totales generales
    total_activos = serializers.IntegerField(
        help_text="Cantidad total de activos activos"
    )

    total_categorias = serializers.IntegerField(
        help_text="Cantidad total de categorías"
    )

    total_ubicaciones = serializers.IntegerField(
        help_text="Cantidad total de ubicaciones"
    )

    valor_total = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Valor total de todos los activos"
    )

    # Datos agrupados (listas)
    activos_por_categoria = serializers.ListField(
        help_text="Lista de activos agrupados por categoría"
    )

    activos_por_ubicacion = serializers.ListField(
        help_text="Lista de activos agrupados por ubicación"
    )

    activos_por_estado = serializers.ListField(
        help_text="Lista de activos agrupados por estado"
    )