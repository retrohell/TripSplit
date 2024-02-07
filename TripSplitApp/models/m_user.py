from django.db import models
import uuid
from django.contrib.auth.models import User

class Guest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='user')