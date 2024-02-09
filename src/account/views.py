from django.contrib.auth import get_user_model
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.response import Response
from . import filters
from . import serializers


class EmployeeList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.EmployeeFilter


class EmployeeCreate(generics.CreateAPIView):
    serializer_class = serializers.EmployeeCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        return Response({'user_id': user.id, 'token': token})


class PasswordReset(generics.GenericAPIView):
    serializer_class = serializers.PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Password has been reset successfully."})
        return Response(serializer.errors, status=400)