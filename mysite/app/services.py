from django.contrib.auth.models import User

from . import models


def get_friends(user: User):
    to_friend_requests = models.FriendRequest.objects.filter(
        to_user=user, accepted=True
    ).select_related("by_user")
    by_friend_requests = models.FriendRequest.objects.filter(
        by_user=user, accepted=True
    ).select_related("to_user")
    for friend in to_friend_requests:
        friend.other_user = friend.by_user
    for friend in by_friend_requests:
        friend.other_user = friend.to_user

    return list(to_friend_requests) + list(by_friend_requests)


def get_direct_message_channels(user: User):
    user1_channels = models.DirectMessageChannel.objects.filter(user1=user)
    user2_channels = models.DirectMessageChannel.objects.filter(user2=user)
    for user1 in user1_channels:
        user1.other_user = user1.user2
    for user2 in user2_channels:
        user2.other_user = user2.user1

    return list(user1_channels) + list(user2_channels)


def server_default_role(server: models.Server):
    return models.Role.objects.create(server=server, default_role=True)
