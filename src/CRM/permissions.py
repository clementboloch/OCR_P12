from rest_framework import permissions
from rest_framework.exceptions import NotFound
from . import models

class IsInGroupNamePermission(permissions.BasePermission):
    def __init__(self, group_name, method, *args, **kwargs):
        self.group_name = group_name
        self.method = method
        super().__init__(*args, **kwargs)

    def has_permission(self, request, view):
        if self.method is None:
            method_permission = True
        else:
            if isinstance(self.method, str):
                method_permission = request.method == self.method
            else:
                method_permission = request.method in list(self.method)

        return request.user.groups.filter(name=self.group_name).exists() and method_permission
    

def is_in_group_name_permission(group_name, method=None):
    class IsInGroupNamePermissionInstance(IsInGroupNamePermission):
        def __init__(self, *args, **kwargs):
            super().__init__(group_name, method, *args, **kwargs)
            
    return IsInGroupNamePermissionInstance


class management_add_contact(permissions.BasePermission):
    def has_permission(self, request, view):
        method = request.method == 'PATCH'
        group = request.user.groups.filter(name='Management').exists()
        data = request.data.keys()
        contact = len(data) == 1 and 'Support contact' in data
        if method and group and contact:
            return True
        else:
            return False


class IsCommercialContactPermission(permissions.BasePermission):
    def __init__(self, Object, method, *args, **kwargs):
        self.Object = Object
        self.method = method
        super().__init__(*args, **kwargs)

    def has_permission(self, request, view):
        if self.method is not None:
            if isinstance(self.method, str):
                method_permission = request.method == self.method
            else:
                method_permission = request.method in list(self.method)
            if method_permission is False:
                return False
        User = request.user
        if not User.groups.filter(name='Commercial').exists():
            return False
        pk = view.kwargs.get('pk')
        if self.Object == models.Client:
            return self.Object.objects.filter(pk=pk, commercial_contact=User).exists()
        elif self.Object == models.Contract:
            contract = self.Object.objects.filter(pk=pk).first()
            if contract is None:
                raise NotFound(detail="Contract not found")
            return contract.client.commercial_contact == User
        elif self.Object == models.Event:
            event = self.Object.objects.filter(pk=pk).first()
            if event is None:
                raise NotFound(detail="Event not found")
            return event.contract.client.commercial_contact == User
        else:
            return False


def is_commercial_contact_permission(Object, method=None):
    class IsCommercialContactPermissionInstance(IsCommercialContactPermission):
        def __init__(self, *args, **kwargs):
            super().__init__(Object, method, *args, **kwargs)
            
    return IsCommercialContactPermissionInstance


class IsSupportContactPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        User = request.user
        if not User.groups.filter(name='Support').exists():
            return False
        pk = request.parser_context.get('kwargs').get('pk')
        event = models.Event.objects.filter(pk=pk).first()
        if event is None:
            raise NotFound(detail="Event not found")
        return event.support_contact == User
