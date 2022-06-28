import time, os, subprocess, re
from Configuration.models import blocklist, mail
import smtplib

class protect:

    mailaddress = mail.objects.all()
    for m in mailaddress:
        mailaddr = m.mail
        mailpass = m.password
    addresses = {}

    def __init__(self,logfilename,error,port,service,process,requestcount):
        self.logfilename = logfilename
        self.error = error
        self.port = port
        self.service = service
        self.process = process
        self.requestcount = requestcount
    
    def monitoring(self):
        logfile = open(f"{self.logfilename}","r")
        loglines = self.follow(logfile)

        for line in loglines:
            if f"{self.error}" in line:
                ip = str(re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",line).group(0))
                self.block(ip)
                print(self.addresses)

    def block(self,ip):
        global addresses
        if self.addresses.get(ip):
            self.addresses[ip] += 1
            if self.addresses[ip] >= int(self.requestcount):
                if blocklist.objects.filter(ip = ip, service = f"{self.service}"):
                    pass
                else:
                    deny = subprocess.check_output(f'sudo killall {self.process}', shell=True)
                    deny = subprocess.check_output(f'sudo ufw insert 1 deny proto tcp from {ip} to any port {self.port}', shell=True)
                    blocklist.objects.create(ip = ip, service = f"{self.service}")
                    deny = subprocess.check_output(f'sudo service {self.process} restart', shell=True)
                    #global mailaddr, mailpass
                    #self.send_email(f"{self.mailaddr}", f"{self.mailpass}", f"Subject: IP {self.service} Servisinden Engellendi \n\n {ip} Adresi engellenmistir.")
                print("engellendi.")
        else:
            self.addresses[ip] = 1

    def follow(self,thefile):

        thefile.seek(0, os.SEEK_END)
        
        while True:

            line = thefile.readline()

            if not line:
                time.sleep(0.0001)
                continue

            yield line

    def send_email(self,email,password,message):
        email_server = smtplib.SMTP("smtp-mail.outlook.com",587)
        email_server.starttls()
        email_server.login(email,password)
        email_server.sendmail(email,email,message)
        email_server.quit()