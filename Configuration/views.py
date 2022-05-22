from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import mail, trycount, blocklist, settings

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
        pass
    else:    
        blocks = blocklist.objects.all()
        context = {
            'blocks':  blocks
        }
        return render(request, "pages/blockedlist.html", context)