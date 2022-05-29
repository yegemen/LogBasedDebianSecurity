from protection import protectCode

logfilename = "/var/log/vsftpd.log"
error = "FAIL LOGIN"
port = 21
service = "FTP"

ftpProtect = protectCode.protect(logfilename,error,port,service)
ftpProtect.monitoring()