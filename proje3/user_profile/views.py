from django.shortcuts import render
#kullanıcı oturumu işlemleri için gerekli modülleri dahil ettik
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Uyeler

# Create your views here.
def login(request):
    baslik = "Oturum Aç"
    sozluk = dict(
        baslik = baslik
    )
    return render(request, "user_profile/login.html", sozluk)

def logout(request):
    pass

def register(request):
    sozluk = dict()
    if(request.method=="POST"):
        post_info = request.POST
        adi = post_info.get("adi")
        soyadi = post_info.get("soyadi")
        eposta = post_info.get("eposta")
        parola =post_info.get("parola")
        parolatekrar = post_info.get("parolatekrar")

        #kontrol mekanizması

        if(parola != parolatekrar):
            print("parola eşleşmiyor")
            messages.info(request, "parola eşleşmiyor")
        # kullanici kontrolunu eposta adresi uzerinden bakıyoruz
        # epostası bulunan kisi yoksa olustur varsa getir 
        user , created = User.object.get_or_create(username = eposta, password = parola)
        if not created:
            userLogin = authenticate(request, username= eposta) 
    return render(request, "user_profile/register.html", sozluk)
