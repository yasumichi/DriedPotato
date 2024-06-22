from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from . import views

app_name="account"
urlpatterns = [
    path("", RedirectView.as_view(url='/items/')),
    path("home/", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password_change", views.PasswordChange.as_view(), name="password_change"),
    path("password_change_done", views.PasswordChangeDone.as_view(), name="password_change_done"),
]
