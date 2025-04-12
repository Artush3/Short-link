from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('we/', views.we, name="we"),
    path('link/', views.ListLink.as_view(), name="link"),
]