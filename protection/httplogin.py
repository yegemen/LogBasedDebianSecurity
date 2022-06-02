from protection import protectCode

logfilename = "/var/log/apache2/error.log"
error = "authentication failure"
port = 80
service = "HTTP"
process = "apache2"

httploginProtect = protectCode.protect(logfilename,error,port,service,process)
httploginProtect.monitoring()