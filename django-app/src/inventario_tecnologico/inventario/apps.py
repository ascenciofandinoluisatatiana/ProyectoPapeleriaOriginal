from django.apps import AppConfig


class InventarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventario'
    verbose_name = 'Gestión de Inventario'

    def ready(self):
        """
        Se ejecuta cuando la aplicación está lista.
        Importa las señales.
        """
        import inventario.signals