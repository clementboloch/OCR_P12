from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound
from .filters import *
from rest_framework import generics, permissions
from . import models
from . import serializers

from .permissions import is_in_group_name_permission, is_commercial_contact_permission, management_add_contact, IsSupportContactPermission

class ClientList(generics.ListAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ClientFilter


class ClientCreate(generics.CreateAPIView):
    permission_classes = [is_in_group_name_permission('Commercial')]
    serializer_class = serializers.ClientCreateSerializer


class ClientModification(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [is_in_group_name_permission('Commercial'), is_commercial_contact_permission(models.Client)]
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
    permission_classes = [is_in_group_name_permission('Management')]
    serializer_class = serializers.ContractCreateSerializer


class ContractModification(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [is_in_group_name_permission('Management')|is_commercial_contact_permission(models.Contract, ['PATCH', 'PUT']),]
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
    permission_classes = [is_commercial_contact_permission(models.Contract)]
    serializer_class = serializers.EventCreateSerializer


class EventModification(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [management_add_contact|IsSupportContactPermission]
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
