from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Server(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    icon = models.FileField()
    created_at = models.DateTimeField(auto_created = True)

class Channel(models.Model):
    class Meta:
        abstract=True
    name = models.CharField(max_length=255)