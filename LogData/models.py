from django.db import models

# Create your models here.

class sshlog(models.Model):
    count = models.CharField(max_length=15)
    date = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    ip = models.CharField(max_length=1000)

class ftplog(models.Model):
    count = models.CharField(max_length=15)
    date = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    ip = models.CharField(max_length=1000)

class authlog(models.Model):
    count = models.CharField(max_length=15)
    date = models.CharField(max_length=1000)
    targetuser = models.CharField(max_length=1000)
    resourceuser = models.CharField(max_length=1000)

class httplog(models.Model):
    count = models.CharField(max_length=15)
    date = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    ip = models.CharField(max_length=1000)

class fuzzinglog(models.Model):
    count = models.CharField(max_length=15)
    ip = models.CharField(max_length=1000)