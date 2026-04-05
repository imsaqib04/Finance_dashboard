from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.permissions import IsAdminUserRole
from .models import User
from .serializers import RegisterSerializer,UserUpdateSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserRoleUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAdminUserRole]  # sirf Admin access kar sakta hai