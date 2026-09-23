from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Crea los grupos de usuarios base del sistema'

    def handle(self, *args, **options):
        grupos = ['Administradores', 'Gestores', 'Consultores']

        for nombre in grupos:
            grupo, creado = Group.objects.get_or_create(name=nombre)
            if creado:
                self.stdout.write(self.style.SUCCESS(f'Grupo creado: {nombre}'))
            else:
                self.stdout.write(f'Grupo ya existía: {nombre}')

        # Consultores: solo permisos de lectura (view)
        grupo_consultores = Group.objects.get(name='Consultores')
        permisos_lectura = Permission.objects.filter(codename__startswith='view_')
        grupo_consultores.permissions.set(permisos_lectura)

        # Gestores: lectura + creación + edición (sin eliminar)
        grupo_gestores = Group.objects.get(name='Gestores')
        permisos_gestor = Permission.objects.filter(
            codename__startswith='view_'
        ) | Permission.objects.filter(
            codename__startswith='add_'
        ) | Permission.objects.filter(
            codename__startswith='change_'
        )
        grupo_gestores.permissions.set(permisos_gestor)

        # Administradores: todos los permisos
        grupo_admin = Group.objects.get(name='Administradores')
        grupo_admin.permissions.set(Permission.objects.all())

        self.stdout.write(self.style.SUCCESS('Grupos y permisos configurados correctamente'))