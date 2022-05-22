from django.contrib import admin
from .models import settings, blocklist, mail, trycount

# Register your models here.

admin.site.register(settings)
admin.site.register(blocklist)
admin.site.register(mail)
admin.site.register(trycount)