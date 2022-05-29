from protection import protectCode

logfilename = "/var/log/apache2/error.log"
error = "authentication failure"
port = 80
service = "HTTP"

httploginProtect = protectCode.protect(logfilename,error,port,service)
httploginProtect.monitoring()