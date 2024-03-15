

from django.shortcuts import redirect, render
#kullanıcı oturum işlemleri için gerekli modüller
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
from django.contrib import messages

from user_profile.models import Uyeler

def login(request):
    baslik = "Oturum Açınız"
    sozluk = dict(
        baslik = baslik,
    )
    if(request.user.is_authenticated):
        messages.info(request, "kişi oturum açtı")
        return redirect("anasayfa")
    #kişi oturum aç sayfasındayken
    if(request.method == "POST"):
        eposta = request.POST.get("eposta")
        parola = request.POST.get("parola")

        user = authenticate(username = eposta, password = parola)

    return render(request,"user_profile/login.html",sozluk)


def logout(request):
    pass

def register(request):
    sozluk = dict()
    if(request.method == "POST"):
        # post olarak değer geliyorsa
        post_info = request.POST
        adi = post_info.get("adi")
        soyadi = post_info.get("soyadi")
        eposta = post_info.get("eposta")
        parola = post_info.get("parola")
        parolatekrar = post_info.get("parolatekrar")

        # kontrol mekanizması
        if(parola != parolatekrar):
            print("parola Eşleşmiyor")
            messages.info(request,"parolalar eşleşmiyor")

        # kullanici kontrolünü eposta adresi üzerinden tanımlıyoruz
        # kullanıcı yoksa oluştur - varsa getir
        user, created = User.objects.get_or_create(username= eposta)

        # kişi zaten üye ise
        if not created:
            userLogin = authenticate(request,username=eposta,password = parola)
            if userLogin is not None:
                messages.success(request,"Hesabınız var.")
                #login oldu
                login(request,userLogin)
                #anasayfaya gönderildi
                return redirect("anasayfa")
            messages.info(request,f" {eposta} kullanıcı oturum açmış. oturum aç ekranına gönderiliyor.")
            return redirect("user_profile:login")
        
        user.email = eposta
        user.first_name=adi
        user.last_name = soyadi
        user.set_password(parola)


        profile, profileCreated = Uyeler.objects.get_or_create(user=user)
        user.save()
        profile.save()
        messages.info(request,f" {eposta} kişi kaydedilmiştir.")
        userLogin = authenticate(request,email=eposta,password=parola)
        return redirect("anasayfa")

    return render(request,"user_profile/register.html",sozluk)
