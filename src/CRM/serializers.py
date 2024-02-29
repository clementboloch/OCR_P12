from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Client


class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['created_date', 'last_update', 'commercial_contact']

    def save(self, **kwargs):
        user = self.context['request'].user
        kwargs['commercial_contact'] = user
        return super().save(**kwargs)


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


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['contract']
        model = Event
    
    def save(self, **kwargs):
        contract_id = self.context['view'].kwargs.get('pk')
        contract = Contract.objects.filter(id=contract_id).first()
        if contract is not None:
            kwargs['contract'] = contract
            return super().save(**kwargs)
        else:
            return super().save(**kwargs)

