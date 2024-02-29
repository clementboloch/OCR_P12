from rest_framework import permissions

class IsInGroupNamePermission(permissions.BasePermission):
    def __init__(self, group_name, *args, **kwargs):
        self.group_name = group_name
        super().__init__(*args, **kwargs)

    def has_permission(self, request, view):
        return request.user.groups.filter(name=self.group_name).exists()
    

def is_in_group_name_permission(group_name):
    class IsInGroupNamePermissionInstance(IsInGroupNamePermission):
        def __init__(self, *args, **kwargs):
            super().__init__(group_name, *args, **kwargs)
            
    return IsInGroupNamePermissionInstance
