from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError


class Categoria(models.Model):
    """
    Modelo para categorizar los activos del inventario.
    
    Ejemplos de categorías:
    - Computadores (COMP)
    - Periféricos (PERIF)
    - Herramientas (HERR)
    - Redes (RED)
    - Consumibles (CONS)
    """
    
    nombre = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(3)],
        help_text="Nombre de la categoría (mínimo 3 caracteres)",
        verbose_name="Nombre de la Categoría"
    )
    
    descripcion = models.TextField(
        blank=True,
        null=True,
        help_text="Descripción detallada de la categoría",
        verbose_name="Descripción"
    )
    
    codigo = models.CharField(
        max_length=10,
        unique=True,
        help_text="Código único de la categoría (ej: COMP, PERIF)",
        verbose_name="Código"
    )
    
    activa = models.BooleanField(
        default=True,
        help_text="Indica si la categoría está activa o inactiva",
        verbose_name="¿Está Activa?"
    )
    
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación",
        help_text="Se asigna automáticamente al crear"
    )
    
    fecha_modificacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última Modificación",
        help_text="Se actualiza automáticamente al modificar"
    )
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']
        db_table = 'inventario_categoria'
        indexes = [
            models.Index(fields=['nombre'], name='idx_categoria_nombre'),
            models.Index(fields=['codigo'], name='idx_categoria_codigo'),
        ]
    
    def clean(self):
        """Validación personalizada del modelo."""
        if self.nombre:
            self.nombre = self._formatear_nombre(self.nombre.strip())
        
        if self.codigo:
            self.codigo = self.codigo.strip().upper()
        
        if self.codigo and ' ' in self.codigo:
            raise ValidationError({
                'codigo': 'El código no puede contener espacios.'
            })

    @staticmethod
    def _formatear_nombre(texto):
        """
        Convierte a formato título, pero dejando en minúscula
        los conectores (y, de, la, el, en, del, para, etc.)
        excepto cuando son la primera palabra.
        """
        conectores = {'y', 'de', 'la', 'el', 'en', 'del', 'para', 'con', 'a', 'o'}
        palabras = texto.lower().split()
        resultado = []
        for i, palabra in enumerate(palabras):
            if i > 0 and palabra in conectores:
                resultado.append(palabra)
            else:
                resultado.append(palabra.capitalize())
        return ' '.join(resultado)
    
    def save(self, *args, **kwargs):
        """Sobrescribir el método save para ejecutar validaciones."""
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        """Representación en string del modelo."""
        return f"{self.codigo} - {self.nombre}"
    
    @property
    def estado(self):
        """Propiedad que retorna el estado en texto."""
        return "Activa" if self.activa else "Inactiva"




class Ubicacion(models.Model):
    """
    Modelo para las ubicaciones físicas donde se almacenan los activos.

    Tipos de ubicaciones:
    - BODEGA: Almacenamiento general
    - LABORATORIO: Laboratorios de formación
    - OFICINA: Oficinas administrativas
    - TALLER: Talleres de mantenimiento
    """

    # Choices para el campo tipo
    TIPO_CHOICES = [
        ('BODEGA', 'Bodega'),
        ('LABORATORIO', 'Laboratorio'),
        ('OFICINA', 'Oficina'),
        ('TALLER', 'Taller'),
    ]

    # CAMPOS DEL MODELO

    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre de la Ubicación",
        help_text="Nombre descriptivo de la ubicación"
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='BODEGA',
        verbose_name="Tipo de Ubicación",
        help_text="Tipo de espacio físico"
    )

    codigo = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Código",
        help_text="Código único (ej: BOD-01, LAB-02)"
    )

    capacidad = models.IntegerField(
        default=0,
        verbose_name="Capacidad",
        help_text="Número máximo de activos"
    )

    responsable = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Responsable",
        help_text="Nombre del responsable"
    )

    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaciones"
    )

    activa = models.BooleanField(
        default=True,
        verbose_name="Activa"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación"
    )

    fecha_modificacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última Modificación"
    )

    # METADATA

    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"
        ordering = ['nombre']
        db_table = 'inventario_ubicacion'
        indexes = [
            models.Index(fields=['nombre'], name='idx_ubicacion_nombre'),
            models.Index(fields=['codigo'], name='idx_ubicacion_codigo'),
        ]

    # MÉTODOS DEL MODELO

    def clean(self):
        """Validación personalizada."""
        from django.core.exceptions import ValidationError

        if self.codigo:
            self.codigo = self.codigo.strip().upper()

        if self.nombre:
            self.nombre = self.nombre.strip().title()

        if self.capacidad < 0:
            raise ValidationError({
                'capacidad': 'La capacidad no puede ser negativa.'
            })

    def save(self, *args, **kwargs):
        """Sobrescribir save para ejecutar validaciones."""
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """Representación en string."""
        return f"{self.codigo} - {self.nombre}"

class Estado(models.Model):
    """
    Modelo para los estados operativos de los activos.

    Estados comunes:
    - OPERATIVO: Funcionando correctamente
    - MANTENIMIENTO: En proceso de mantenimiento
    - REPARACION: En reparación
    - BAJA: Dado de baja
    - RESERVADO: Reservado para uso específico
    """

    # CAMPOS DEL MODELO

    nombre = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Nombre del Estado"
    )

    codigo = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Código",
        help_text="Código único (ej: OPER, MANT, REP)"
    )

    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción"
    )

    color = models.CharField(
        max_length=7,
        default='#6c757d',
        verbose_name="Color",
        help_text="Color hexadecimal (ej: #28a745)"
    )

    es_operativo = models.BooleanField(
        default=True,
        verbose_name="Es Operativo",
        help_text="¿El activo en este estado está operativo?"
    )

    requiere_accion = models.BooleanField(
        default=False,
        verbose_name="Requiere Acción",
        help_text="¿Requiere alguna acción o seguimiento?"
    )

    orden = models.IntegerField(
        default=0,
        verbose_name="Orden",
        help_text="Orden de prioridad (menor = más prioritario)"
    )

    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación"
    )

    fecha_modificacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última Modificación"
    )

    # METADATA

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['orden', 'nombre']
        db_table = 'inventario_estado'

    # MÉTODOS

    def clean(self):
        """Validación personalizada."""
        from django.core.exceptions import ValidationError

        if self.codigo:
            self.codigo = self.codigo.strip().upper()

        if self.nombre:
            self.nombre = self.nombre.strip().title()

        if self.color:
            self.color = self.color.strip()
            if not self.color.startswith('#'):
                raise ValidationError({
                    'color': 'El color debe empezar con # (ej: #28a745)'
                })
            if len(self.color) != 7:
                raise ValidationError({
                    'color': 'El color debe tener formato #RRGGBB'
                })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Activo(models.Model):
    """
    Modelo principal para los activos del inventario.
    """

    # CAMPOS BÁSICOS

    codigo_inventario = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Código de Inventario",
        help_text="Código único (ej: ACT-2024-001)"
    )

    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre del Activo"
    )

    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción"
    )

    # RELACIONES FOREIGN KEY

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='activos',
        verbose_name="Categoría"
    )

    ubicacion = models.ForeignKey(
        Ubicacion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='activos',
        verbose_name="Ubicación"
    )

    estado = models.ForeignKey(
        Estado,
        on_delete=models.PROTECT,
        related_name='activos',
        verbose_name="Estado"
    )

    # INFORMACIÓN DEL PRODUCTO

    marca = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Marca"
    )

    modelo = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Modelo"
    )

    numero_serie = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Número de Serie"
    )

    # INFORMACIÓN FINANCIERA

    fecha_adquisicion = models.DateField(
        blank=True,
        null=True,
        verbose_name="Fecha de Adquisición"
    )

    valor_adquisicion = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Valor de Adquisición"
    )

    # GESTIÓN

    responsable = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Responsable"
    )

    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaciones"
    )

    # IMAGEN

    foto = models.ImageField(
        upload_to='activos/fotos/%Y/%m/',
        blank=True,
        null=True,
        verbose_name="Fotografía"
    )

    # CONTROL

    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación"
    )

    fecha_modificacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última Modificación"
    )

    class Meta:
        verbose_name = "Activo"
        verbose_name_plural = "Activos"
        ordering = ['-fecha_creacion']
        db_table = 'inventario_activo'

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.codigo_inventario:
            self.codigo_inventario = self.codigo_inventario.strip().upper()

        if self.valor_adquisicion is not None and self.valor_adquisicion < 0:
            raise ValidationError({
                'valor_adquisicion': 'No puede ser negativo.'
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo_inventario} - {self.nombre}"

    def get_valor_formateado(self):
        if self.valor_adquisicion:
            return f"${self.valor_adquisicion:,.0f}"
        return "N/A"


class HistorialMovimiento(models.Model):
    """
    Registra el historial de movimientos de activos.

    Cada cambio de ubicación crea un registro para trazabilidad.
    """

    # Choices para motivo
    MOTIVO_CHOICES = [
        ('TRASLADO', 'Traslado Normal'),
        ('MANTENIMIENTO', 'Envío a Mantenimiento'),
        ('PRESTAMO', 'Préstamo Temporal'),
        ('REASIGNACION', 'Reasignación Permanente'),
        ('DEVOLUCION', 'Devolución'),
        ('OTRO', 'Otro Motivo'),
    ]

    # CAMPOS

    activo = models.ForeignKey(
        Activo,
        on_delete=models.CASCADE,
        related_name='historial_movimientos',
        verbose_name="Activo"
    )

    ubicacion_origen = models.ForeignKey(
        Ubicacion,
        on_delete=models.PROTECT,
        related_name='movimientos_salida',
        null=True,
        blank=True,
        verbose_name="Ubicación Origen"
    )

    ubicacion_destino = models.ForeignKey(
        Ubicacion,
        on_delete=models.PROTECT,
        related_name='movimientos_entrada',
        verbose_name="Ubicación Destino"
    )

    fecha_movimiento = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Movimiento"
    )

    usuario = models.CharField(
        max_length=200,
        verbose_name="Usuario"
    )

    motivo = models.CharField(
        max_length=20,
        choices=MOTIVO_CHOICES,
        default='TRASLADO',
        verbose_name="Motivo"
    )

    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaciones"
    )

    aprobado = models.BooleanField(
        default=True,
        verbose_name="Aprobado"
    )

    # METADATA

    class Meta:
        verbose_name = "Historial de Movimiento"
        verbose_name_plural = "Historial de Movimientos"
        ordering = ['-fecha_movimiento']
        db_table = 'inventario_historial_movimiento'

    def __str__(self):
        origen = self.ubicacion_origen.nombre if self.ubicacion_origen else "N/A"
        return f"{self.activo.codigo_inventario}: {origen} → {self.ubicacion_destino.nombre}"


class Mantenimiento(models.Model):
    """
    Registra mantenimientos de activos.

    Tipos: Preventivos (programados) y Correctivos (reparaciones).
    """

    # Choices
    TIPO_CHOICES = [
        ('PREVENTIVO', 'Mantenimiento Preventivo'),
        ('CORRECTIVO', 'Mantenimiento Correctivo'),
    ]

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('COMPLETADO', 'Completado'),
        ('CANCELADO', 'Cancelado'),
    ]

    # CAMPOS

    activo = models.ForeignKey(
        Activo,
        on_delete=models.CASCADE,
        related_name='mantenimientos',
        verbose_name="Activo"
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        verbose_name="Tipo"
    )

    fecha_inicio = models.DateField(
        verbose_name="Fecha de Inicio"
    )

    fecha_fin = models.DateField(
        blank=True,
        null=True,
        verbose_name="Fecha de Finalización"
    )

    tecnico = models.CharField(
        max_length=200,
        verbose_name="Técnico"
    )

    costo = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Costo"
    )

    descripcion = models.TextField(
        verbose_name="Descripción"
    )

    repuestos = models.TextField(
        blank=True,
        null=True,
        verbose_name="Repuestos"
    )

    estado_mantenimiento = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='PENDIENTE',
        verbose_name="Estado"
    )

    observaciones = models.TextField(
        blank=True,
        null=True
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    # METADATA

    class Meta:
        verbose_name = "Mantenimiento"
        verbose_name_plural = "Mantenimientos"
        ordering = ['-fecha_inicio']
        db_table = 'inventario_mantenimiento'

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.activo.codigo_inventario}"

    def get_costo_formateado(self):
        if self.costo:
            return f"${self.costo:,.2f}"
        return "N/A"


"""
=========================================
MODELO DE PERFIL DE USUARIO
=========================================
"""

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    """
    Perfil extendido de usuario.
    
    Extiende el modelo User de Django con información adicional
    específica del sistema de inventario.
    """
    
    CARGOS = [
        ('ADMIN', 'Administrador'),
        ('COORD', 'Coordinador'),
        ('TEC', 'Técnico'),
        ('AUX', 'Auxiliar'),
    ]
    
    DEPARTAMENTOS = [
        ('TI', 'Tecnología e Informática'),
        ('ADM', 'Administrativo'),
        ('MTO', 'Mantenimiento'),
        ('LOG', 'Logística'),
    ]
    
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    cargo = models.CharField(
        max_length=10,
        choices=CARGOS,
        default='AUX'
    )
    departamento = models.CharField(
        max_length=10,
        choices=DEPARTAMENTOS,
        default='TI'
    )
    telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    foto = models.ImageField(
        upload_to='perfiles/',
        blank=True,
        null=True
    )
    biografia = models.TextField(
        blank=True,
        default='',
        verbose_name='Biografía',
        help_text='Breve descripción del usuario'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['usuario__username']
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
    def get_nombre_completo(self):
        """Obtener nombre completo del usuario."""
        if self.usuario.first_name and self.usuario.last_name:
            return f"{self.usuario.first_name} {self.usuario.last_name}"
        return self.usuario.username


# Señales para crear/actualizar perfil automáticamente
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """Crear perfil automáticamente cuando se crea un usuario."""
    if created:
        Perfil.objects.create(usuario=instance)


@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    """Guardar perfil cuando se guarda el usuario."""
    Perfil.objects.get_or_create(usuario=instance)
    instance.perfil.save()


"""
=========================================
MODELO DE AUDITORÍA (LOG)
=========================================
"""

from django.contrib.auth.models import User
from django.db import models


class Log(models.Model):
    """Registro de auditoría del sistema."""
    
    ACCIONES = [
        ('CREATE', 'Crear'),
        ('UPDATE', 'Actualizar'),
        ('DELETE', 'Eliminar'),
        ('VIEW', 'Ver'),
        ('LOGIN', 'Iniciar Sesión'),
        ('LOGOUT', 'Cerrar Sesión'),
        ('EXPORT', 'Exportar'),
        ('IMPORT', 'Importar'),
    ]
    
    # Quien
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='logs')
    usuario_nombre = models.CharField(max_length=150)
    
    # Qué
    accion = models.CharField(max_length=20, choices=ACCIONES)
    modelo = models.CharField(max_length=100)
    objeto_id = models.CharField(max_length=100, blank=True, null=True)
    objeto_repr = models.CharField(max_length=200, blank=True)
    
    # Cuándo
    fecha_hora = models.DateTimeField(auto_now_add=True)
    
    # Detalles
    descripcion = models.TextField(blank=True)
    datos_anteriores = models.JSONField(null=True, blank=True)
    datos_nuevos = models.JSONField(null=True, blank=True)
    
    # Contexto técnico
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, blank=True)
    
    class Meta:
        verbose_name = 'Log de Auditoría'
        verbose_name_plural = 'Logs de Auditoría'
        ordering = ['-fecha_hora']
        indexes = [
            models.Index(fields=['-fecha_hora']),
            models.Index(fields=['usuario', '-fecha_hora']),
            models.Index(fields=['modelo', '-fecha_hora']),
        ]
    
    def __str__(self):
        return f"{self.usuario_nombre} - {self.get_accion_display()} - {self.modelo}"
    
    @classmethod
    def registrar(cls, usuario, accion, modelo, objeto=None, descripcion='', 
                  datos_anteriores=None, datos_nuevos=None, request=None):
        """Método helper para crear logs fácilmente."""
        log = cls(
            usuario=usuario if usuario.is_authenticated else None,
            usuario_nombre=usuario.username if usuario.is_authenticated else 'Anónimo',
            accion=accion,
            modelo=modelo,
            descripcion=descripcion,
            datos_anteriores=datos_anteriores,
            datos_nuevos=datos_nuevos,
        )
        
        if objeto:
            log.objeto_id = str(objeto.pk)
            log.objeto_repr = str(objeto)
        
        if request:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                log.ip_address = x_forwarded_for.split(',')[0]
            else:
                log.ip_address = request.META.get('REMOTE_ADDR')
            log.user_agent = request.META.get('HTTP_USER_AGENT', '')[:255]
        
        log.save()
        return log