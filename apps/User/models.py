# serializers.py
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()
    phone = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    house_number = serializers.CharField()
    apartment_number = serializers.CharField(required=False)
    language = serializers.CharField(required=False)
