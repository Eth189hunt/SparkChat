from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("account/login/", views.LoginUser.as_view(), name="login"),
    path("account/register/", views.RegisterUser.as_view(), name="register"),
    path("account/logout/", views.LogoutUser.as_view(), name="logout"),
]
