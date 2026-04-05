from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True) 
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_email(self, value):
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data,
            role=User.Role.VIEWER
        )
        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['role', 'is_active']

    def validate_role(self, value):
        # Sirf valid roles allowed hain
        if value not in [User.Role.VIEWER, User.Role.ANALYST, User.Role.ADMIN]:
            raise serializers.ValidationError("Invalid role.")
        return value