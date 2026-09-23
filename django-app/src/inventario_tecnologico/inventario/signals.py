"""
Señales de Django para el módulo de inventario.
"""

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Activo, HistorialMovimiento


@receiver(pre_save, sender=Activo)
def registrar_cambio_ubicacion(sender, instance, **kwargs):
    """
    Se ejecuta ANTES de guardar un Activo.
    Detecta si cambió la ubicación.
    """
    if instance.pk:
        try:
            activo_anterior = Activo.objects.get(pk=instance.pk)

            if activo_anterior.ubicacion != instance.ubicacion:
                instance._ubicacion_cambio = True
                instance._ubicacion_anterior = activo_anterior.ubicacion
        except Activo.DoesNotExist:
            pass


@receiver(post_save, sender=Activo)
def crear_historial_movimiento(sender, instance, created, **kwargs):
    """
    Se ejecuta DESPUÉS de guardar.
    Crea el registro en historial si hubo cambio.
    """
    if hasattr(instance, '_ubicacion_cambio') and instance._ubicacion_cambio:
        HistorialMovimiento.objects.create(
            activo=instance,
            ubicacion_origen=instance._ubicacion_anterior,
            ubicacion_destino=instance.ubicacion,
            usuario='Sistema',
            motivo='TRASLADO',
            observaciones='Registrado automáticamente'
        )

        delattr(instance, '_ubicacion_cambio')
        delattr(instance, '_ubicacion_anterior')


@receiver(post_save, sender=Activo)
def notificar_creacion_activo(sender, instance, created, **kwargs):
    """Notifica cuando se crea un nuevo activo."""
    if created:
        print(f"✓ Nuevo activo: {instance.codigo_inventario}")