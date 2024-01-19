from django.contrib.auth.models import User, Group
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


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)


class EmployeeSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        fields = ['first_name', 'last_name', 'email', 'date_joined', 'groups']
        model = User
