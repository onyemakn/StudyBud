from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room")
    # path('', views.home, name="home")
    # path('', views.home, name="home")
    # path('', views.home, name="home")
]
