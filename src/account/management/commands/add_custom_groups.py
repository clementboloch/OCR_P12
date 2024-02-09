from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Creates custom groups with specific permissions'

    def handle(self, *args, **options):
        all_view_permissions_codenames = [
            'view_client', 'view_contract', 'view_event'
        ]
        
        management_permissions_codenames = [
            'add_employee', 'change_employee', 'delete_employee',
            'add_contract', 'change_contract',
            'change_event'
        ]
        
        commercial_permissions_codenames = [
            'add_client', 'change_client',
            'change_contract',
            'add_event'
        ]
        
        support_permissions_codenames = [
            'change_event'
        ]
        
        def create_group_with_permissions(group_name, permissions_codenames):
            group, created = Group.objects.get_or_create(name=group_name)
            for codename in permissions_codenames:
                try:
                    permission = Permission.objects.get(codename=codename)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Permission {codename} does not exist.'))
            return created
        
        if create_group_with_permissions('Management', management_permissions_codenames + all_view_permissions_codenames):
            self.stdout.write(self.style.SUCCESS('Successfully created or updated "Management" group'))
        
        if create_group_with_permissions('Commercial', commercial_permissions_codenames + all_view_permissions_codenames):
            self.stdout.write(self.style.SUCCESS('Successfully created or updated "Commercial" group'))
        
        if create_group_with_permissions('Support', support_permissions_codenames + all_view_permissions_codenames):
            self.stdout.write(self.style.SUCCESS('Successfully created or updated "Support" group'))
