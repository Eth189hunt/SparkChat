from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("server/create/", views.ServerCreateView.as_view(), name="server-create"),
    path(
        "server/<int:server_pk>/",
        views.ServerDetailView.as_view(),
        name="server-detail",
    ),
    path(
        "server/<int:server_pk>/channel/create/",
        views.CreateTextChannelView.as_view(),
        name="channel-create",
    ),
    path(
        "server/<int:server_pk>/channel/<int:textchannel_pk>/",
        views.TextChannelMessageCreateView.as_view(),
        name="channel-detail",
    ),
    path("requests/", views.FriendRequestListView.as_view(), name="friend-requests"),
    path(
        "requests/create/",
        views.FriendRequestCreateView.as_view(),
        name="friend-request-create",
    ),
    path(
        "requests/<int:request_pk>/",
        views.FriendRequestUpdateView.as_view(),
        name="friend-request-update",
    ),
    path(
        "direct/<int:user_pk>/",
        views.DirectMessageCreateView.as_view(),
        name="direct-message",
    ),
]
