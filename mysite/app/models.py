from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Server(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    icon = models.FileField()
    created_at = models.DateTimeField(auto_created=True)


class Channel(models.Model):
    class Meta:
        abstract = True
    unique_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)


class Role(models.Model):
    unique_id = models.AutoField(primary_key=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    permission_server_edit = models.BooleanField(default=False)
    roles_edit = models.BooleanField(default=False)
    roles_member_manage = models.BooleanField(default=False)
    permission_channels_read = models.BooleanField(default=False)
    permissions_channels_write = models.BooleanField(default=False)
    permission_channels_manage = models.BooleanField(default=False)


class Message(models.Model):
    unique_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_created=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

# Don't even know if this should be a model? Maybe a form instead?
# class FriendRequest(models.Model):
#     unique_id = models.AutoField(primary_key=True)
#     by_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     to_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     accepted = models.BooleanField(default=False)
