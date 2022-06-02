from protection import protectCode

logfilename = "/var/log/apache2/access.log"
error = "404"
port = 80
service = "HTTP"
process = "apache2"

httpfuzzingProtect = protectCode.protect(logfilename,error,port,service,process)
httpfuzzingProtect.monitoring()