from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView ,UserRoleUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/<int:pk>/update/', UserRoleUpdateView.as_view(), name='user-role-update'),
]


#flow
# Register karo  →  hamesha VIEWER banta hai
# Admin login karo  →  kisi bhi user ka role change karo
# Koi bhi khud se Admin nahi ban sakta ✅