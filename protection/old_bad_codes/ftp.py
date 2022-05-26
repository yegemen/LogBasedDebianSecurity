from protection import protectCodes

command = 'grep "FAIL LOGIN" /var/log/vsftpd.log | cut -d " " -f 12 | sort | uniq -c | sort'
port = "21"
service = "FTP"

ftpProtect = protectCodes.protectRe(command,port,service)
ftpProtect.monitoring()