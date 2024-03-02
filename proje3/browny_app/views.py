from django.shortcuts import render
from .models import *

# Create your views here.
def anasayfa(request):
    haberler = Haberler.objects.all()
    baslik = "Anasayfa"
    sozluk = dict(
        baslik = baslik,
        haberler = haberler
    )
    return render(request,"sayfalar/index.html", sozluk)

def egitimler(request, egitimID):
    ## pk değeri gelecek
    egitimid = Haberler.objects.get(pk=egitimID)
    baslik = "Eğitimler"
    sozluk = dict(
        baslik = baslik,
        egitimid = egitimid
    )
    return render(request, "sayfalar/egitimler.html", sozluk)