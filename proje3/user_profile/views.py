from django.shortcuts import render, redirect
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
        user , created = User.object.get_or_create(username = eposta)
        if not created:
            userLogin = authenticate(request, username= eposta, password = parola)
            if userLogin is not None:
                messages.success(request, "daha önceden kaydiniz bulunmaktadir")
                login(request, userLogin) # login olmuş bir şekilde anasayfaya gönderdik
                return redirect("anasayfa") 
            messages.info(request, f"{eposta} kişisi önceden kayit olmus oturum aç ekranina gönderiliyor")
            return redirect("user_profile:login")
        
        user.email = eposta
        user.first_name = adi
        user.last_name = soyadi
        user.set_passworn(parola)

        #bilgileri kaybettik
        profile, profileCreated = Uyeler.objects.get_or_create(user = user)
        user.save()
        profile.save()

        messages.info(request, "kişi kaydedilmiştir.")
        userLogin = authenticate(request, email = eposta, password = parola)
        return redirect("anasayfa")

    return render(request, "user_profile/register.html", sozluk)
