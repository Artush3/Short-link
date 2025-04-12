from django.urls import path
from . import views
from django.contrib.auth import views as UserViews

urlpatterns = [
    path('', views.reg, name="reg"),
    path('login', UserViews.LoginView.as_view(template_name="user/login.html"), name="login"),
    path('exit', UserViews.LogoutView.as_view(template_name="user/exit.html"), name="exit"),
    path('profil', views.profil, name="profil"),
]