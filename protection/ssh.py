from protection import protectCode

logfilename = "/var/log/auth.log"
error = "Failed password"
port = 22
service = "SSH"
process = "sshd"

sshProtect = protectCode.protect(logfilename,error,port,service,process)
sshProtect.monitoring()