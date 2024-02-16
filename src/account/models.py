from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from datetime import date

class EmployeeManager(BaseUserManager):
    use_in_migrations = True


class Employee(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(default=date.today)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    group_name = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)

    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        groups = self.groups.values_list('name',flat = True)
        if groups:
            group = groups[0]
        else:
            group = "No team"
        return f"{self.first_name} {self.last_name} - {group}"
