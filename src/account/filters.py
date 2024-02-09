from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model


class EmployeeFilter(filters.FilterSet):
    no_first_name = filters.BooleanFilter(field_name='first_name', lookup_expr='isnull')
    no_last_name = filters.BooleanFilter(field_name='last_name', lookup_expr='isnull')
    no_email = filters.BooleanFilter(field_name='email', lookup_expr='isnull')
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
