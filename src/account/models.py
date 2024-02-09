from django.db import models
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from datetime import date

class EmployeeManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, group_name=None, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_staff = True
        user.is_active = False
        # user.save()
        if password:
            user.set_password(password)
            user.is_active = True
        user.save(using=self._db)
        
        if group_name:
            try:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
            except Group.DoesNotExist:
                raise ValidationError(f"The group '{group_name}' does not exist.")

        return user

    def create_superuser(self, email, group_name=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, group_name, password, **extra_fields)


class Employee(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    group_name = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    birthdate = models.DateField(default=date.today)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.group_name}"
