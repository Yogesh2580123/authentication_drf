from django.db import models
from django.conf import settings



class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
