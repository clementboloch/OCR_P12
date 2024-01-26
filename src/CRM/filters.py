from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from .models import *


class ClientFilter(filters.FilterSet):
    min_created_date = filters.DateFilter(field_name='created_date', lookup_expr='gte')
    max_created_date = filters.DateFilter(field_name='created_date', lookup_expr='lte')

    no_email = uncategorized = filters.BooleanFilter(field_name='email', lookup_expr='isnull')

    class Meta:
        model = Client
        fields = '__all__'


class ContractFilter(filters.FilterSet):
    min_created_date = filters.DateFilter(field_name='created_date', lookup_expr='gte')
    max_created_date = filters.DateFilter(field_name='created_date', lookup_expr='lte')

    min_amount = filters.NumberFilter(field_name="amount", lookup_expr='gte')
    max_amount = filters.NumberFilter(field_name="amount", lookup_expr='lte')

    min_outstading_amount = filters.NumberFilter(field_name="outstanding_amount", lookup_expr='gte')
    max_outstading_amount = filters.NumberFilter(field_name="outstanding_amount", lookup_expr='lte')

    no_amount = uncategorized = filters.BooleanFilter(field_name='amount', lookup_expr='isnull')
    no_phone = filters.BooleanFilter(field_name='phone', lookup_expr='isnull')
    no_company = filters.BooleanFilter(field_name='company', lookup_expr='isnull')
    no_commercial_contact = filters.BooleanFilter(field_name='commercial_contact', lookup_expr='isnull')

    class Meta:
        model = Contract
        fields = '__all__'


class EventFilter(filters.FilterSet):
    min_start_date = filters.DateFilter(field_name='start_date', lookup_expr='gte')
    max_start_date = filters.DateFilter(field_name='start_date', lookup_expr='lte')
    
    min_end_date = filters.DateFilter(field_name='end_date', lookup_expr='gte')
    max_end_date = filters.DateFilter(field_name='end_date', lookup_expr='lte')

    min_attendees = filters.NumberFilter(field_name="attendees", lookup_expr='gte')
    max_attendees = filters.NumberFilter(field_name="attendees", lookup_expr='lte')

    no_start_date = filters.BooleanFilter(field_name='start_date', lookup_expr='isnull')
    no_end_date = filters.BooleanFilter(field_name='end_date', lookup_expr='isnull')
    no_location = filters.BooleanFilter(field_name='location', lookup_expr='isnull')
    no_attendees = filters.BooleanFilter(field_name='attendees', lookup_expr='isnull')
    no_notes = filters.BooleanFilter(field_name='notes', lookup_expr='isnull')
    no_support_contact = filters.BooleanFilter(field_name='support_contact', lookup_expr='isnull')

    class Meta:
        model = Event
        fields = '__all__'


class EmployeeFilter(filters.FilterSet):
    no_first_name = filters.BooleanFilter(field_name='first_name', lookup_expr='isnull')
    no_last_name = filters.BooleanFilter(field_name='last_name', lookup_expr='isnull')
    no_email = filters.BooleanFilter(field_name='email', lookup_expr='isnull')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
