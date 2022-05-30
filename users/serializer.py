from pyexpat import model
from rest_framework import serializers
from .models import UserRegistration
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ('id', 'username',
                  'email', 'password', 'date_joined', 'is_superuser')
        write_only_fields = ('password')

    def create(self, validated_data):
        user = UserRegistration(

            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],

        )
        user.set_password(validated_data['password'])

        user.save()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        # ...
        return token
