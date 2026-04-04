from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # Yahan se 'role' hata diya hai taaki user input na de sake
        fields = ['username', 'email', 'password'] 

    def create(self, validated_data):
        # Backend forcibly 'VIEWER' role hi set karega naye open registrations ke liye
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            role='VIEWER' # Hardcoded default for safety
        )
        return user