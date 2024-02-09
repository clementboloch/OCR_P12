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

    is_fully_paid = filters.BooleanFilter(field_name='outstanding_amount', lookup_expr='exact', method='filter_fully_paid')

    def filter_fully_paid(self, queryset, name, value):
        if value:
            return queryset.filter(**{name: 0})
        return queryset

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
