from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

# kullanıcı giriş
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # kontrol burda yapılıyor.
        user = auth.authenticate(username=username, password=password)
        if user is not None:  # user objesi none değilse
            auth.login(request, user)  # session id oluşturur
            #messages.add_message(request, messages.SUCCESS, "Oturum Açıldı")
            return redirect('select')
        else:
            messages.add_message(request, messages.ERROR, "Error !")
            return redirect('login')
    else:
        return render(request, 'pages/login.html')

# kullanıcı kayıt
def register(request):
    if request.method == 'POST':

        # bilgileri alıyorum

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:  # parolalar uyuşuyorsa
            # veritabanında aynı kullanıcı var mı diye bakıyorum. eğer varsa true bilgi gelir.
            if User.objects.filter(username=username).exists():
                messages.add_message(
                    request, messages.WARNING, "This Username Has Been Taken Before.")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(
                        request, messages.WARNING, "This E-Mail Has Been Received Before.")
                    return redirect('register')
                else:
                    # herşey tamam
                    user = User.objects.create_user(
                        username=username, password=password, email=email)  # burda veritabanına kullanıcı bilgilerini gönderdim.
                    user.save()
                    messages.add_message(
                        request, messages.SUCCESS, "Your Account Has Been Created.")
                    return redirect('login')

        else:
            messages.add_message(request, messages.WARNING,
                                 "Passwords Do Not Match.")
            return redirect('register')

    else:
        return render(request, 'pages/register.html')

def select(request):
    return render(request, "pages/select.html")

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS,
                             'Your session has been closed.')
        return redirect('login')