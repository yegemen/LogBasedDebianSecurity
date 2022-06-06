from protection import protectCode
from Configuration.models import trycount

deger = trycount.objects.filter(service = "SSH")
for d in deger:
    count = d.trycount

logfilename = "/var/log/auth.log"
error = "Failed password"
port = 22
service = "SSH"
process = "sshd"

sshProtect = protectCode.protect(logfilename,error,port,service,process,count)
sshProtect.monitoring()