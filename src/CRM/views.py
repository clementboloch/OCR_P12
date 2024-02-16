from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework import generics, permissions
from . import models
from . import serializers

class ClientList(generics.ListAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ClientFilter


class ClientCreate(generics.CreateAPIView):
    serializer_class = serializers.ClientCreateSerializer


class ClientModification(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

    serializer_class_post = serializers.ClientCreateSerializer

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return super().get_serializer_class()
        else:
            return self.serializer_class_post


class ContractList(generics.ListAPIView):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ContractFilter


class ContractCreate(generics.CreateAPIView):
    serializer_class = serializers.ContractCreateSerializer


class ContractModification(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer

    serializer_class_post = serializers.ContractCreateSerializer

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return super().get_serializer_class()
        else:
            return self.serializer_class_post


class EventList(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter


class EventCreate(generics.CreateAPIView):
    serializer_class = serializers.EventSerializer


class EventModification(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
