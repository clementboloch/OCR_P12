from django.urls import path
from .views import *

urlpatterns = [
    path('client-list/', ClientList.as_view(), name='client-list'),
    path('client-create/', ClientCreate.as_view(), name='client-create'),
    path('contract-list/', ContractList.as_view(), name='contract-list'),
    path('contract-create/', ContractCreate.as_view(), name='contract-create'),
    path('event-list/', EventList.as_view(), name='event-list'),
    path('event-create/', EventCreate.as_view(), name='event-create'),
    path('employee-list/', EmployeeList.as_view(), name='employee-list'),
    path('employee-create/', EmployeeCreate.as_view(), name='employee-create'),
]
