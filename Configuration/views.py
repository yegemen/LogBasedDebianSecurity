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
            trycount.objects.all().delete()
            requesttrycount = request.POST['trycount']
            trycount.objects.create(trycount=requesttrycount)
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
        blocklist.objects.filter(ip = ip).delete()

        if service == "SSH":
            delete_rule = subprocess.check_output(f'sudo ufw delete deny proto tcp from {ip} to any port 22', shell=True)
            delete_log = subprocess.check_output(f"sudo sed '/{ip}/d' /var/log/auth.log -i", shell=True)

        if service == "FTP":
            pass

        if service == "HTTP":
            pass

        return redirect('blockedlist')

    else:    
        blocks = blocklist.objects.all()
        context = {
            'blocks':  blocks
        }
        return render(request, "pages/blockedlist.html", context)