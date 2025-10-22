from django.db import models
from django.contrib.auth.models import AbstractUser

Roles = [
    ("USER", "USER"),
    ("ADMIN", "ADMIN")
]

class RegisterUser(AbstractUser):
    role = models.CharField(max_length=20, choices=Roles, default="USER")

    def save(self, *args, **kwargs):
        if self.is_staff or self.is_superuser:
            self.role = "ADMIN"
        else:
            self.role = "USER"
        return super().save(*args, **kwargs)