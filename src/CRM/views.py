from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework import generics
from . import models
from . import serializers

class ClientList(generics.ListAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ClientFilter


class ClientCreate(generics.CreateAPIView):
    serializer_class = serializers.ClientCreateSerializer


class ContractList(generics.ListAPIView):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ContractFilter


class ContractCreate(generics.CreateAPIView):
    serializer_class = serializers.ContractCreateSerializer


class EventList(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter


class EventCreate(generics.CreateAPIView):
    serializer_class = serializers.EventSerializer
