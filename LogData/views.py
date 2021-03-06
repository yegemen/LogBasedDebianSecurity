from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import sshlog, ftplog, authlog, httplog, fuzzinglog, summaryssh, summaryftp, summaryhttp, summaryfuzzing, summaryauth
import subprocess, re

# Create your views here.

def sshlist(request):
    
    sshlog.objects.all().delete()
    summaryssh.objects.all().delete()

    commandone = subprocess.check_output('grep "Failed password for" /var/log/auth.log | grep "invalid user" -v | grep "TTY=pts/0" -v | cut -d " " -f 1,2,3,9,11 | sort | uniq -c | sort -rn', shell=True).decode("utf-8")
    commandtwo = subprocess.check_output('grep "Failed password for" /var/log/auth.log | grep "invalid user" | cut -d " " -f 1,2,3,11,13 | sort | uniq -c | sort -rn', shell=True).decode("utf-8")
    commandthree = subprocess.check_output('( (grep "Failed password for" /var/log/auth.log | grep "invalid user" -v | grep "TTY=pts/0" -v | cut -d " " -f 9,11) && (grep "Failed password for" /var/log/auth.log | grep "invalid user" | cut -d " " -f 11,13) ) | grep "Failed" -v | sort | uniq -c | sort -rn', shell=True).decode('utf-8')

    print(commandone)
    
    for data in commandone.splitlines():
        data = data.split()
        print(data[0] + " " + data[1] + " " + data[2] + " " + data[3] + " " + data[4] + " " + data[5])
        sshlog.objects.create(count = data[0], date = (data[1] + " " + data[2] + " " + data[3]), username = data[4], ip = data[5])

    for data in commandtwo.splitlines():
        data = data.split()
        print(data[0] + " " + data[1] + " " + data[2] + " " + data[3] + " " + data[4] + " " + data[5])
        sshlog.objects.create(count = data[0], date = (data[1] + " " + data[2] + " " + data[3]), username = data[4], ip = data[5])

    for data in commandthree.splitlines():
        data = data.split()
        summaryssh.objects.create(sumcount = data[0], username = data[1], ip = data[2])

    log = sshlog.objects.all()
    sumlog = summaryssh.objects.all()

    context = {
        'log': log,
        'sumlog': sumlog
    }

    return render(request, "pages/sshlist.html", context)

def ftplist(request):

    ftplog.objects.all().delete()
    summaryftp.objects.all().delete()

    command = subprocess.check_output('grep "FAIL LOGIN" /var/log/vsftpd.log | cut -d " " -f 1,2,3,4,5,8,12 | sort | uniq -c | sort', shell=True).decode("utf-8")
    commandsum = subprocess.check_output('grep "FAIL LOGIN" /var/log/vsftpd.log | cut -d " " -f 8,12 | sort | uniq -c | sort', shell=True).decode("utf-8")
    
    for data in command.splitlines():
        data = data.split()
        data[7] = str(re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",data[7]).group(0))
        ftplog.objects.create(count = data[0], date = (data[1] + " " + data[2] + " " + data[3] + " " + data[4] + " " + data[5]), username = data[6], ip = data[7])

    for data in commandsum.splitlines():
        data = data.split()
        data[2] = str(re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",data[2]).group(0))
        summaryftp.objects.create(sumcount = data[0], username = data[1], ip = data[2])

    log = ftplog.objects.all()
    sumlog = summaryftp.objects.all()

    context = {
        'log': log,
        'sumlog': sumlog
    }

    return render(request, "pages/ftplist.html", context)

def authlist(request):

    authlog.objects.all().delete()
    summaryauth.objects.all().delete()

    command = subprocess.check_output('grep "FAILED SU" /var/log/auth.log | cut -d " " -f 1,2,3,8,9,10 | sort | uniq -c | sort -rn', shell=True).decode("utf-8")
    commandsum = subprocess.check_output('grep "FAILED SU" /var/log/auth.log | cut -d " " -f 8,9,10 | sort | uniq -c | sort -rn', shell=True).decode("utf-8")
    
    for data in command.splitlines():
        data = data.split()
        authlog.objects.create(count = data[0], date = (data[1] + " " + data[2] + " " + data[3]), targetuser = (data[4] + " " + data[5]), resourceuser = data[6])

    for data in commandsum.splitlines():
        data = data.split()
        summaryauth.objects.create(sumcount = data[0], targetuser = (data[1] + " " + data[2]), resourceuser = data[3])

    log = authlog.objects.all()
    sumlog = summaryauth.objects.all()

    context = {
        'log': log,
        'sumlog': sumlog
    }

    return render(request, "pages/authlist.html",context)

def httplist(request):

    httplog.objects.all().delete()
    summaryhttp.objects.all().delete()

    command = subprocess.check_output('(grep "authentication failure" /var/log/apache2/error.log && grep "not found" /var/log/apache2/error.log) | cut -d " " -f 1,2,3,4,5,11,14 | sort | uniq -c | sort -rn', shell=True).decode("utf-8")
    commandsum = subprocess.check_output('(grep "authentication failure" /var/log/apache2/error.log && grep "not found" /var/log/apache2/error.log) | cut -d " " -f 11,14 | sort | uniq -c | sort -rn', shell=True).decode("utf-8")
    
    for data in command.splitlines():
        data = data.split()
        data[6] = str(re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",data[6]).group(0))
        httplog.objects.create(count = data[0], date = (data[1] + " " + data[2] + " " + data[3] + " " + data[4] + " " + data[5]), username = data[7], ip = data[6])
    
    for data in commandsum.splitlines():
        data = data.split()
        data[1] = str(re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",data[1]).group(0))
        summaryhttp.objects.create(sumcount = data[0], ip = data[1], username = data[2])

    log = httplog.objects.all()
    sumlog = summaryhttp.objects.all()

    context = {
        'log': log,
        'sumlog': sumlog
    }
    return render(request, "pages/httplist.html", context)

def fuzzinglist(request):

    fuzzinglog.objects.all().delete()
    summaryfuzzing.objects.all().delete()

    command = subprocess.check_output('grep "404" /var/log/apache2/access.log | cut -d " " -f 1,4 | sort | uniq -c | sort -rn', shell=True).decode("utf-8")
    commandsum = subprocess.check_output('grep "404" /var/log/apache2/access.log | cut -d " " -f 1 | sort | uniq -c | sort -rn', shell=True).decode("utf-8")
    
    for data in command.splitlines():
        data = data.split()
        fuzzinglog.objects.create(count = data[0], ip = data[1], date = data[2])
    
    for data in commandsum.splitlines():
        data = data.split()
        summaryfuzzing.objects.create(sumcount = data[0], ip = data[1])

    log = fuzzinglog.objects.all()
    sumlog = summaryfuzzing.objects.all()

    context = {
        'log': log,
        'sumlog': sumlog
    }

    return render(request, "pages/fuzzinglist.html",context)