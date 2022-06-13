from django.contrib import admin

from LogData.models import sshlog
from .models import sshlog, ftplog, authlog, httplog, fuzzinglog, summaryssh, summaryftp, summaryhttp, summaryfuzzing, summaryauth

# Register your models here.

admin.site.register(sshlog)
admin.site.register(ftplog)
admin.site.register(authlog)
admin.site.register(httplog)
admin.site.register(fuzzinglog)
admin.site.register(summaryssh)
admin.site.register(summaryftp)
admin.site.register(summaryhttp)
admin.site.register(summaryfuzzing)
admin.site.register(summaryauth)