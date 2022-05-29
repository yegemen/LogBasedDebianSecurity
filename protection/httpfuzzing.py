from protection import protectCode

logfilename = "/var/log/apache2/access.log"
error = "404"
port = 80
service = "HTTP"

httpfuzzingProtect = protectCode.protect(logfilename,error,port,service)
httpfuzzingProtect.monitoring()