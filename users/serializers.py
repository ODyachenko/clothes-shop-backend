from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile

class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password',)


class ReviewAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class UserInfoSerializer(UserSerializer):
    street_address = serializers.CharField(source='profile.street_address')
    city = serializers.CharField(source='profile.city')
    state = serializers.CharField(source='profile.state')
    zip_code = serializers.CharField(source='profile.zip_code')
    name = serializers.CharField(source='profile.name')
    number = serializers.CharField(source='profile.number')
    cvc = serializers.CharField(source='profile.cvc')
    expiry = serializers.CharField(source='profile.expiry')

    class Meta(UserSerializer.Meta):
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'name', 'number', 'expiry', 'cvc')