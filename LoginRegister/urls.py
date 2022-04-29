from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('select/', views.select, name='select'),
    path('logout/', views.logout, name= 'logout'),
]