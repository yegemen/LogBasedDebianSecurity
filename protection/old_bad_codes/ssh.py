from protection import protectCodes

command = '( (grep "Failed password for" /var/log/auth.log | grep "invalid user" -v | grep "TTY=pts/0" -v | cut -d " " -f 11) && (grep "Failed password for" /var/log/auth.log | grep "invalid user" | cut -d " " -f 13) ) | grep "Failed" -v | sort | uniq -c | sort -rn'
port = "22"
service = "SSH"

sshProtect = protectCodes.protect(command,port,service)
sshProtect.monitoring()