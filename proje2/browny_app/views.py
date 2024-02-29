from django.shortcuts import render
from .models import *

# Create your views here.

def anasayfa(request):
    haberler  = Haberler.objects.all()
    baslik = "Anasayfa"    
    sozluk = dict(
        baslik = baslik,
        haberler = haberler
    )

    return render(request, "sayfalar/index.html", sozluk)

def egitimler(request, egitimID):
    #pk degeri gelecek
    egitimid = Haberler.objects.get(pk = egitimID)
    baslik = "egitimler"
    sozluk = dict(
        baslik = baslik,
        egitimid = egitimid
    )
    return render(request, "sayfalar/egitimler.html", sozluk)
















