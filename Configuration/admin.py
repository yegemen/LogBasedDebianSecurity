from django.contrib import admin
from .models import settings, blocklist

# Register your models here.

admin.site.register(settings)
admin.site.register(blocklist)
