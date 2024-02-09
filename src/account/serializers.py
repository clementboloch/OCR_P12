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
        fields = ['first_name', 'last_name', 'email', 'date_joined', 'groups']
        model = get_user_model()


class EmployeeCreateSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = ['email', 'group_name', 'first_name', 'last_name', 'birthdate']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_group_name(self, value):
        if value:
            try:
                group = Group.objects.get(name=value)
            except Group.DoesNotExist:
                raise serializers.ValidationError("This group does not exist.")
            return group
        return None

    def create(self, validated_data):
        group_data = validated_data.pop('group_name', None)
        user = super().create(validated_data)
        if group_data:
            user.group_name = group_data
            user.save()
        return user



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
        email = self.validated_data['email']
        new_password = self.validated_data['new_password']
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.is_active = True
        user.save()