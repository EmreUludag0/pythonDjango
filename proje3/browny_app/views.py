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

def haberler(request):
    haberler = Haberler.objects.all()
    baslik = "Haberler"
    sozluk = dict(
        baslik = baslik,
        haberler = haberler
    )
    return render(request, "sayfalar/haberler.html", sozluk)

def haberdetay(request, haberID):
    ## pk değeri gelecek
    haberler = Haberler.objects.get(pk=haberID)
    baslik = "Haber Detay"
    sozluk = dict(
        baslik = baslik,
        haberler = haberler
    )
    return render(request, "sayfalar/haberdetay.html", sozluk)