from django.db import models

# Create your models here.

class settings(models.Model):
    mail = models.CharField(max_length=100)
    trycount = models.CharField(max_length=10)

class mail(models.Model):
    mail = models.CharField(max_length=100)

class trycount(models.Model):
    trycount = models.CharField(max_length=10)

class blocklist(models.Model):
    date = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
