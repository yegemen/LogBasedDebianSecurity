import subprocess
import re
from Configuration.models import blocklist

class protect():
    
    def __init__(self,command,port,service):
        self.command = command
        self.port = port
        self.service = service
    
    def monitoring(self):
        print(f"Started {self.service} protect")
        while True:

            data = subprocess.check_output(self.command, shell=True).decode("utf-8")
            
            for dt in data.splitlines():
                dt = dt.split()
                if int(dt[0]) >= 5:
                    if blocklist.objects.filter(ip = dt[1], service = self.service):
                        continue
                    else:
                        deny = subprocess.check_output(f'sudo ufw insert 1 deny proto tcp from {dt[1]} to any port {self.port}', shell=True)
                        blocklist.objects.create(ip = dt[1], service = f"{self.service}")

class protectRe(protect):
    
    def __init__(self,command,port,service):
        protect.__init__(self,command,port,service)
        
    def monitoring(self):
        print(f"Started {self.service} protect")
        while True:

            data = subprocess.check_output(self.command, shell=True).decode("utf-8")
            
            for dt in data.splitlines():
                dt = dt.split()
                dt[1] = str(re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",dt[1]).group(0))
                if int(dt[0]) >= 5:
                    if blocklist.objects.filter(ip = dt[1], service = self.service):
                        continue
                    else:
                        deny = subprocess.check_output(f'sudo ufw insert 1 deny proto tcp from {dt[1]} to any port {self.port}', shell=True)
                        blocklist.objects.create(ip = dt[1], service = f"{self.service}")