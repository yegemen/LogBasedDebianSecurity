from protection import protectCode
from Configuration.models import trycount

deger = trycount.objects.filter(service = "HTTP")
for d in deger:
    count = d.trycount

logfilename = "/var/log/apache2/error.log"
error = "authentication failure"
port = 80
service = "HTTP"
process = "apache2"

httploginProtect = protectCode.protect(logfilename,error,port,service,process,count)
httploginProtect.monitoring()