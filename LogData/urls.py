from django.urls import path
from . import views

urlpatterns = [
    path('sshlist/', views.sshlist, name='sshlist'),
    path('ftplist/', views.ftplist, name='ftplist'),
    path('authlist/', views.authlist, name='authlist'),
    path('httplist/', views.httplist, name='httplist'),
    path('fuzzinglist/', views.fuzzinglist, name='fuzzinglist'),
]