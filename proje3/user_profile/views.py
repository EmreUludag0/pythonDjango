from django.shortcuts import render

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
    baslik = "Üyelik Oluştur"
    sozluk = dict(
        baslik = baslik
    )
    return render(request, "user_profile/register.html", sozluk)