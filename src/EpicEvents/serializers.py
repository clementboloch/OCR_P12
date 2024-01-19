from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class UserRegistrationSerializer(serializers.ModelSerializer):
    group = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'group']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        group = validated_data.pop('group', None)

        try:
            group = Group.objects.get(name=group)
            user = User.objects.create_user(**validated_data)
            user.is_staff = True
            user.save()
            user.groups.add(group)
        except Group.DoesNotExist:
            raise ValidationError(f"The group '{group}' does not exist.")

        return user
