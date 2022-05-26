import subprocess
import re

data = subprocess.check_output('grep "FAIL LOGIN" /var/log/vsftpd.log | cut -d " " -f 12 | sort | uniq -c | sort', shell=True).decode("utf-8")

data = data.split()

data[1] = str(re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",data[1]).group(0))

print(data[1])