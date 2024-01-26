from django.urls import path
from .views import *

urlpatterns = [
    path('client-list/', ClientList.as_view(), name='client-list'),
    path('contract-list/', ContractList.as_view(), name='contract-list'),
    path('event-list/', EventList.as_view(), name='event-list'),
    path('employee-list/', EmployeeList.as_view(), name='employee-list'),
]
