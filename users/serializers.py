from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True) 
    class Meta:
        model = User
        fields = ['username', 'email', 'password','first_name','last_name']

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

class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['role'] = user.role
        token['email'] = user.email

        return token
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['role', 'is_active']

    def validate_role(self, value):
        if value not in [User.Role.VIEWER, User.Role.ANALYST, User.Role.ADMIN]:
            raise serializers.ValidationError("Invalid role.")
        return value