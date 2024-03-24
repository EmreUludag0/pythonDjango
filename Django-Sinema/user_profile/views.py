from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  # herhangi bir kullanıcı ekliyoruz SINIF
from .models import Profile  # veritabanı işlemi için dahil ettik


# Create your views here.


def profilView(request):
    icerik = dict()
    return render(request, "user_profile/profilim.html", icerik)


def loginView(request):
    if(request.user.is_authenticated):
        messages.info(request, "{} - Sisteme Giriş Yaptı".format(request.user.username))
        return redirect("anasayfa")
    
    icerik = dict()
    
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        # print(username, password)  # terminalde bilgileri alıp almadığı kontrolü
        
        if (len(username) < 8 or len(password) < 3):
            messages.warning(request, "Kullanıcı Adı veya Parola\n8 Karakterden az olamaz!")
            return redirect("user_profile:loginView")
        
        user = authenticate(request, username=username, password=password)
        
        # kontrol kısmını
        if (user is not None):
            login(request, user)
            messages.success(request, "{} - Oturum Açtı".format(request.user.username))
            return redirect('anasayfa')
    
    return render(request, "user_profile/login.html", icerik)


def logoutView(request):
    messages.info(request, "{} - Oturumunu Kapattı".format(request.user.username))
    logout(request)
    return redirect('anasayfa')

def registerView(request):
    icerik = dict()
    if (request.method == "POST"):
        post_info = request.POST
        print(post_info)

        # register bilgileri atamasını yaptık
        adi = post_info.get("adi")
        soyadi = post_info.get("soyadi")
        eposta = post_info.get("eposta")
        eposta_confirm = post_info.get("eposta_confirm")
        parola = post_info.get("parola")
        parola_confirm = post_info.get("parola_confirm")
        
        # parola ve kullanıcıAdi kontrol
        if(len(adi) < 3 or len(soyadi) < 3 or len(eposta) < 3 or len(parola) < 3 ):
            messages.warning(request, "Bilgiler 3 karakterden az olamaz")
            return redirect('user_profile:registerView')

        if (eposta != eposta_confirm):
            messages.warning(request, "E-Posta Adresleri Eşleşmiyor")
            return redirect('user_profile:registerView')
        
        if (parola != parola_confirm):
            messages.warning(request, "Parolalar Eşleşmiyor")
            return redirect('user_profile:registerView')

        user, created = User.objects.get_or_create(username=eposta)
        
        if not created:
            userLogin = authenticate(request, username=eposta, password=parola)
            if(userLogin is not None):
                messages.success(request, "Daha Önce Kayıt Olmuşsunuz\nAnasayfaya Yönlendiriliyorsunuz")
                login(request, userLogin)
                return redirect("anasayfa")
            
            messages.warning(request, f"{eposta} adresi sisteme kayıtlı ama giriş yapamadınız\nLogin Yönlendiriliyor")
            return redirect ("user_profile:loginView")
        # veritabanına kullanıcı ekliyoruz
        user.email = eposta
        user.first_name= adi
        user.last_name = soyadi
        user.set_password(parola)
        
        profile, profileCreated = Profile.objects.get_or_create(user=user)
        user.save()
        profile.save()
        
        messages.success(request, f"{user.first_name} - Sisteme kaydedildi")
        userLogin = authenticate(request, username=eposta, password=parola)
        login(request, userLogin)
        return redirect("anasayfa")
        
    return render(request, "user_profile/register.html", icerik)