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
]
