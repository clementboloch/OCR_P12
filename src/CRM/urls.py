from django.urls import path
from .views import *
from account.views import *

urlpatterns = [
    path('client-list/', ClientList.as_view(), name='client-list'),
    path('client-create/', ClientCreate.as_view(), name='client-create'),
    path('client-modify/<int:pk>/', ClientModification.as_view(), name='client-modify'),
    path('contract-list/', ContractList.as_view(), name='contract-list'),
    path('contract-create/', ContractCreate.as_view(), name='contract-create'),
    path('contract-modify/<int:pk>/', ContractModification.as_view(), name='contract-modify'),
    path('contract-add-event/<int:pk>/', EventCreate.as_view(), name='contract-add-event'),
    path('event-list/', EventList.as_view(), name='event-list'),
    path('event-modify/<int:pk>/', EventModification.as_view(), name='event-modify'),

    # from account app
    path('employee-list/', EmployeeList.as_view(), name='employee-list'),
    path('employee-create/', EmployeeCreate.as_view(), name='employee-create'),
    path('employee-modify/<int:pk>/', EmployeeModification.as_view(), name='employee-modify'),
]
