from django.contrib.auth.models import User
from django.db import models


class Server(models.Model):
    owner = models.ForeignKey(
        User, related_name="server_owner", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name="server_members")
    name = models.CharField(max_length=255)
    icon = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    invite_link = models.CharField(max_length=65, null=True, blank=True)


class Channel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255)


class Message(models.Model):
    class Meta:
        abstract = True

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def created_at_str(self):
        return self.created_at.strftime("%b %d %Y at %H:%M")


class DirectMessageChannel(Channel):
    user1 = models.ForeignKey(
        User, related_name="directmessage_user1", on_delete=models.CASCADE
    )
    user2 = models.ForeignKey(
        User, related_name="directmessage_user2", on_delete=models.CASCADE
    )

    def name(self):
        return f"{self.user1.username}, {self.user2.username}"


class DirectMessage(Message):
    channel = models.ForeignKey(
        DirectMessageChannel,
        related_name="directmessage_channel",
        on_delete=models.CASCADE,
    )


class TextChannel(Channel):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)


class TextChannelMessage(Message):
    channel = models.ForeignKey(
        TextChannel, related_name="textchannel_channel", on_delete=models.CASCADE
    )


class Role(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="role_members")
    default_role = models.BooleanField(default=False)
    permission_server_edit = models.BooleanField(default=False)
    roles_edit = models.BooleanField(default=False)
    roles_member_manage = models.BooleanField(default=False)
    permission_channels_read = models.BooleanField(default=False)
    permissions_channels_write = models.BooleanField(default=False)
    permission_channels_manage = models.BooleanField(default=False)


class FriendRequest(models.Model):
    by_user = models.ForeignKey(
        User, related_name="friendrequest_by_user", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User, related_name="friendrquest_to_user", on_delete=models.CASCADE
    )
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def created_at_str(self):
        return self.created_at.strftime("%b %d %Y")
