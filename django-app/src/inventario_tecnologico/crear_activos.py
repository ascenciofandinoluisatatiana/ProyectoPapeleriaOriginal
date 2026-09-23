from inventario.models import Activo, Categoria, Ubicacion, Estado
from datetime import date
from decimal import Decimal

def crear(codigo, **kwargs):
    obj, creado = Activo.objects.get_or_create(
        codigo_inventario=codigo, defaults=kwargs
    )
    estado_txt = "creado" if creado else "ya existia, se omitio"
    print(f"{codigo}: {estado_txt}")
    return obj

cat_impr = Categoria.objects.get(codigo='IMPR')
ubi_ofi = Ubicacion.objects.get(codigo='OFI-SIS-01')
est_oper = Estado.objects.get(codigo='OPER')

crear('ACT-2024-003',
    nombre='Impresora HP LaserJet',
    descripcion='Impresora laser multifuncional',
    categoria=cat_impr, ubicacion=ubi_ofi, estado=est_oper,
    marca='HP', modelo='LaserJet Pro M404', numero_serie='HP2024003',
    fecha_adquisicion=date(2024, 3, 5),
    valor_adquisicion=Decimal('1200000.00'),
    responsable='Carlos Ramirez',
)

cat_herr = Categoria.objects.get(codigo='HERR')
ubi_taller = Ubicacion.objects.get(codigo='TAL-MAN-01')
est_mant = Estado.objects.get(codigo='MANT')

crear('ACT-2024-004',
    nombre='Taladro Industrial',
    descripcion='Taladro de banco para taller',
    categoria=cat_herr, ubicacion=ubi_taller, estado=est_mant,
    marca='Bosch', modelo='GBM 32-4', numero_serie='BOSCH2024004',
    fecha_adquisicion=date(2023, 11, 20),
    valor_adquisicion=Decimal('650000.00'),
    responsable='Luis Torres',
    observaciones='En mantenimiento preventivo programado.',
)

cat_perif = Categoria.objects.get(codigo='PERIF')
ubi_bod2 = Ubicacion.objects.get(codigo='BOD-02')
est_resv = Estado.objects.get(codigo='RESV')

crear('ACT-2024-005',
    nombre='Teclado Mecanico Logitech',
    descripcion='Teclado reservado para nuevo puesto de trabajo',
    categoria=cat_perif, ubicacion=ubi_bod2, estado=est_resv,
    marca='Logitech', modelo='MX Keys', numero_serie='LOGI2024005',
    fecha_adquisicion=date(2024, 4, 12),
    valor_adquisicion=Decimal('320000.00'),
    responsable='Sofia Gomez',
)

print("Listo.")
