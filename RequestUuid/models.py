from django.db import models
from uuid import uuid4

# Create your models here.


class UUIDGenerator(models.Model):
    cached_response = models.TextField(default='{}')

    def __str__(self):
        return f"{self.cached_response}"
