from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.permissions import IsAdminUserRole
from .models import User
from .serializers import RegisterSerializer,UserUpdateSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            return Response(
                {
                    "success": True,
                    "message": "User registered successfully!",
                    "data": {
                        "username": user.username,
                        "email": user.email
                    }
                }, 
                status=status.HTTP_201_CREATED
            )
            
        return Response(
            {
                "success": False,
                "message": "Registration failed",
                "errors": serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )

class UserRoleUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAdminUserRole]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                {
                    "success": True,
                    "message": f"User ID {instance.id} role/status updated successfully!",
                    "data": serializer.data
                }, 
                status=status.HTTP_200_OK
            )
            
        return Response(
            {
                "success": False,
                "message": "Failed to update user.",
                "errors": serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )


class CustomLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            return Response({
                "success": True,
                "message": "Login successful!",
                "data": serializer.validated_data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "success": False,
                "message": "Invalid username or password. Please try again.",
                "errors": {"detail": str(e)}
            }, status=status.HTTP_401_UNAUTHORIZED)