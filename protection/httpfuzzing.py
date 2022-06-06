from protection import protectCode
from Configuration.models import trycount

deger = trycount.objects.filter(service = "HTTP")
for d in deger:
    count = d.trycount

logfilename = "/var/log/apache2/access.log"
error = "404"
port = 80
service = "HTTP"
process = "apache2"

httpfuzzingProtect = protectCode.protect(logfilename,error,port,service,process,count)
httpfuzzingProtect.monitoring()