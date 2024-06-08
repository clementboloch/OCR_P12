from django.contrib.auth.models import Group, Permission
import pytest

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
            print(f"Permission with codename '{codename}' does not exist.")
    return created

@pytest.fixture(scope='session', autouse=True)
def setup_groups(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        create_group_with_permissions('Management', management_permissions_codenames + all_view_permissions_codenames)
        create_group_with_permissions('Commercial', commercial_permissions_codenames + all_view_permissions_codenames)
        create_group_with_permissions('Support', support_permissions_codenames + all_view_permissions_codenames)
