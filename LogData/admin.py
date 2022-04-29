from django.contrib import admin

from LogData.models import sshlog
from .models import sshlog, ftplog, authlog, httplog, fuzzinglog

# Register your models here.

admin.site.register(sshlog)
admin.site.register(ftplog)
admin.site.register(authlog)
admin.site.register(httplog)
admin.site.register(fuzzinglog)