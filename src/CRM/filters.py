from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from .models import *


class ClientFilter(filters.FilterSet):
    min_created_date = filters.DateFilter(field_name='created_date', lookup_expr='gte')
    max_created_date = filters.DateFilter(field_name='created_date', lookup_expr='lte')

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

    class Meta:
        model = Event
        fields = '__all__'


class EmployeeFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
