import subprocess

command = subprocess.check_output('( (grep "Failed password for" /var/log/auth.log | grep "invalid user" -v | grep "TTY=pts/0" -v | cut -d " " -f 11) && (grep "Failed password for" /var/log/auth.log | grep "invalid user" | cut -d " " -f 13) ) | grep "Failed" -v | sort | uniq -c | sort -rn', shell=True).decode("utf-8")

print(command)

while True:
    command = subprocess.check_output('( (grep "Failed password for" /var/log/auth.log | grep "invalid user" -v | grep "TTY=pts/0" -v | cut -d " " -f 11) && (grep "Failed password for" /var/log/auth.log | grep "invalid user" | cut -d " " -f 13) ) | grep "Failed" -v | sort | uniq -c | sort -rn', shell=True).decode("utf-8")
    for data in command.splitlines():
        if int(data[0]) >= 5:
            deny = subprocess.check_output(f'sudo ufw insert 1 deny proto tcp from {data[1]} to any port 22', shell=True)


data = command.split()
print(data[0] + "== >" + data[1])