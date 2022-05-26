from protection import protectCode

logfilename = "/var/log/auth.log"
error = "Failed password"
port = 22
service = "SSH"

sshProtect = protectCode.protect(logfilename,error,port,service)
sshProtect.monitoring()