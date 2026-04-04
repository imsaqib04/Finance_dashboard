from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    # Admin panel ki table mein kya kya columns dikhane hain
    list_display = ['username', 'email', 'role', 'is_staff']
    
    # User ki detail open karne par 'role' ka option dikhane ke liye
    fieldsets = UserAdmin.fieldsets + (
        ('Role Management', {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)