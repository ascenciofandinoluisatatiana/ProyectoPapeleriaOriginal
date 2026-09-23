"""
Generador de reportes en PDF usando ReportLab.
"""
import os
from datetime import datetime
from django.conf import settings
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
)


def _carpeta_reportes():
    """Crea (si no existe) y retorna la carpeta donde se guardan los PDFs."""
    carpeta = os.path.join(settings.MEDIA_ROOT, 'reportes')
    os.makedirs(carpeta, exist_ok=True)
    return carpeta


def generar_reporte_inventario_general(activos):
    """
    Genera un PDF con el listado general de activos.
    Recibe un queryset de Activo y retorna la ruta del archivo generado.
    """
    nombre_archivo = f'inventario_general_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    ruta = os.path.join(_carpeta_reportes(), nombre_archivo)

    doc = SimpleDocTemplate(
        ruta,
        pagesize=landscape(letter),
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
    )

    estilos = getSampleStyleSheet()
    estilo_titulo = ParagraphStyle(
        'TituloReporte',
        parent=estilos['Title'],
        fontSize=16,
        spaceAfter=12,
    )

    elementos = []
    elementos.append(Paragraph('Reporte de Inventario General', estilo_titulo))
    elementos.append(Paragraph(
        f'Generado el {datetime.now().strftime("%d/%m/%Y %H:%M")} - '
        f'Total de activos: {activos.count()}',
        estilos['Normal']
    ))
    elementos.append(Spacer(1, 0.5 * cm))

    encabezados = ['Código', 'Nombre', 'Categoría', 'Ubicación', 'Estado', 'Valor']
    datos = [encabezados]

    for activo in activos:
        datos.append([
            activo.codigo_inventario,
            activo.nombre,
            str(activo.categoria) if activo.categoria else '-',
            str(activo.ubicacion) if activo.ubicacion else '-',
            str(activo.estado) if activo.estado else '-',
            f'${activo.valor_adquisicion:,.0f}' if activo.valor_adquisicion else '$0',
        ])

    tabla = Table(datos, repeatRows=1)
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#00324D')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f2f2f2')]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))

    elementos.append(tabla)
    doc.build(elementos)

    return ruta


def generar_reporte_activos_por_ubicacion(activos):
    """
    Genera un PDF con los activos agrupados por ubicación.
    Recibe un queryset de Activo y retorna la ruta del archivo generado.
    """
    nombre_archivo = f'activos_por_ubicacion_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    ruta = os.path.join(_carpeta_reportes(), nombre_archivo)

    doc = SimpleDocTemplate(
        ruta,
        pagesize=landscape(letter),
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
    )

    estilos = getSampleStyleSheet()
    estilo_titulo = ParagraphStyle(
        'TituloReporte',
        parent=estilos['Title'],
        fontSize=16,
        spaceAfter=12,
    )
    estilo_subtitulo = ParagraphStyle(
        'SubtituloUbicacion',
        parent=estilos['Heading2'],
        fontSize=12,
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.HexColor('#00324D'),
    )

    elementos = []
    elementos.append(Paragraph('Reporte de Activos por Ubicación', estilo_titulo))
    elementos.append(Paragraph(
        f'Generado el {datetime.now().strftime("%d/%m/%Y %H:%M")}',
        estilos['Normal']
    ))
    elementos.append(Spacer(1, 0.3 * cm))

    # Agrupar activos por ubicación en Python
    ubicaciones = {}
    for activo in activos:
        nombre_ubicacion = str(activo.ubicacion) if activo.ubicacion else 'Sin ubicación'
        ubicaciones.setdefault(nombre_ubicacion, []).append(activo)

    for nombre_ubicacion, lista_activos in ubicaciones.items():
        elementos.append(Paragraph(
            f'{nombre_ubicacion} ({len(lista_activos)} activos)',
            estilo_subtitulo
        ))

        datos = [['Código', 'Nombre', 'Categoría', 'Estado', 'Valor']]
        for activo in lista_activos:
            datos.append([
                activo.codigo_inventario,
                activo.nombre,
                str(activo.categoria) if activo.categoria else '-',
                str(activo.estado) if activo.estado else '-',
                f'${activo.valor_adquisicion:,.0f}' if activo.valor_adquisicion else '$0',
            ])

        tabla = Table(datos, repeatRows=1)
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#39A900')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        elementos.append(tabla)
        elementos.append(Spacer(1, 0.4 * cm))

    doc.build(elementos)

    return ruta