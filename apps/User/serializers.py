# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = User.objects.filter(email=email).first()

            if user:
                if user.check_password(password):
                    if user.is_active:
                        return data
                    else:
                        raise serializers.ValidationError("Your account is not active.")
                else:
                    raise serializers.ValidationError("Invalid credentials.")
            else:
                raise serializers.ValidationError("User with this email does not exist.")
        else:
            raise serializers.ValidationError("Email and password are required fields.")

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

    def validate(self, data):
        password = data.get('password')
        repeat_password = data.get('repeat_password')

        if password != repeat_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data
