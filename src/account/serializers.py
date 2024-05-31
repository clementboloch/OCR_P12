from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import *


User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)

class EmployeeSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'email', 'date_joined', 'groups']

class EmployeeCreateSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'birthdate', 'group_name', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def validate_group_name(self, value):
        if value:
            if not Group.objects.filter(name=value).exists():
                raise serializers.ValidationError("This group does not exist.")
        return Group.objects.filter(name=value).first()

    def create(self, validated_data):
        group_name = validated_data.get('group_name', None)
        user = super().create(validated_data)
        user.is_active = False
        if validated_data.get('password'):
            user.set_password(validated_data['password'])
            user.is_active = True
        user.save()

        if group_name:
            group = Group.objects.get(name=group_name)
            user.groups.add(group)

        return user

    def update(self, instance, validated_data):
        group_name = validated_data.get('group_name', None)
        super().update(instance, validated_data)

        if group_name:
            group = Group.objects.get(name=group_name)
            instance.groups.clear()
            instance.groups.add(group)

        return self.instance


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    new_password = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
            if not PasswordResetTokenGenerator().check_token(user, data['token']):
                raise serializers.ValidationError("Invalid token")
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid user")

        return data

    def save(self):
        user = User.objects.get(email=self.validated_data['email'])
        user.set_password(self.validated_data['new_password'])
        user.is_active = True
        user.save()
