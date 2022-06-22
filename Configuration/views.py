from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import mail, trycount, blocklist, settings
import subprocess

# Create your views here.

def settings(request):
    if request.method == 'POST':
        select = request.POST['select']
        if select == "Mail Güncelle":
            mail.objects.all().delete()
            email = request.POST['mail']
            mail.objects.create(mail=email)
        else:
            ssh = request.POST['SSH']
            ftp = request.POST['FTP']
            httplogin = request.POST['HTTP Login']
            httpfuzzing = request.POST['HTTP Fuzzing']
            if ssh == "selecting":
                pass
            else:
                trycount.objects.filter(service="SSH").update(trycount=f"{ssh}")
            if ftp == "selecting":
                pass
            else:
                trycount.objects.filter(service="FTP").update(trycount=f"{ftp}")
            if httplogin == "selecting":
                pass
            else:
                trycount.objects.filter(service="HTTP Login").update(trycount=f"{httplogin}")
            if httpfuzzing == "selecting":
                pass
            else:
                trycount.objects.filter(service="HTTP Fuzzing").update(trycount=f"{httpfuzzing}")
        return redirect('settings')
    else:   
        email =  mail.objects.all()
        requesttrycount =  trycount.objects.all()
        context = {
            'mail':  email,
            'try': requesttrycount
        }
        return render(request, "pages/settings.html", context)
        

def blockedlist(request):
    if request.method == 'POST':
        ip = request.POST['noblock']
        service = request.POST['service']

        if service == "SSH":
            delete_rule = subprocess.check_output(f'sudo ufw delete deny proto tcp from {ip} to any port 22', shell=True)
            blocklist.objects.filter(ip = ip, service = service).delete()

        if service == "FTP":
            delete_rule = subprocess.check_output(f'sudo ufw delete deny proto tcp from {ip} to any port 21', shell=True)
            blocklist.objects.filter(ip = ip, service = service).delete()

        if service == "HTTP":
            delete_rule = subprocess.check_output(f'sudo ufw delete deny proto tcp from {ip} to any port 80', shell=True)
            blocklist.objects.filter(ip = ip, service = service).delete()

        return redirect('blockedlist')

    else:    
        blocks = blocklist.objects.all()
        context = {
            'blocks':  blocks
        }
        return render(request, "pages/blockedlist.html", context)