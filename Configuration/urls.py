from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.settings, name='settings'),
    path('blockedlist/', views.blockedlist, name='blockedlist'),
]