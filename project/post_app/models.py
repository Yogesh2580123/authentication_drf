from django.db import models
from django.conf import settings
from django.utils import timezone



class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    create_at = models.DateTimeField(auto_now_add=True, db_index=True)
    update_at = models.DateTimeField(auto_now=True)
