from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    class Role(models.TextChoices):  # Role, User ke andar hai
        VIEWER = 'VIEWER', 'Viewer'
        ANALYST = 'ANALYST', 'Analyst'
        ADMIN = 'ADMIN', 'Admin'

    # Role class ke BAAD, lekin User class ke ANDAR
    role = models.CharField(
        max_length=10, 
        choices=Role.choices, 
        default=Role.VIEWER
    )

    def __str__(self):
        return f"{self.username} - {self.role}"