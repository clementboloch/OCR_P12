from django.contrib.auth.models import User
from rest_framework import generics
from . import models
from . import serializers

class ClientList(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class ContractList(generics.ListAPIView):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer


class EventList(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class EmployeList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.EmployeeSerializer
