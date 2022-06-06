from protection import protectCode
from Configuration.models import trycount

deger = trycount.objects.filter(service = "FTP")
for d in deger:
    count = d.trycount

logfilename = "/var/log/vsftpd.log"
error = "FAIL LOGIN"
port = 21
service = "FTP"
process = "vsftpd"

ftpProtect = protectCode.protect(logfilename,error,port,service,process,count)
ftpProtect.monitoring()