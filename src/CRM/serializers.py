from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Client


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_date', 'last_update']
        model = Client


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Contract


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['created_date']
        model = Contract


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Event
