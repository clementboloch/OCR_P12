from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework import generics
from . import models
from . import serializers

class ClientList(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ClientFilter


class ContractList(generics.ListAPIView):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ContractFilter


class EventList(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter


class EmployeeList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EmployeeFilter
