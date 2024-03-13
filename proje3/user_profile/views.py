from django.shortcuts import render

# Create your views here.

def loagin(request):
    baslik = "Oturum Aç"
    sozluk = dict(
        baslik = baslik
    )
    return render(request, "user_profile/login.html", sozluk)

def logout(request):
    pass

def register(request):
    baslik = "uyelik olustur"
    sozluk = dict(
        baslik = baslik
    )
    return render(request, "user_profile/register.html", sozluk)

