from django.shortcuts import render
from .models import *


# Create your views here.
def anasayfa(request):
    fotolar = Galeri.objects.all()
    sayfaBaslik = "Anasayfa".upper()
    icerik = dict(
        sayfaBaslik=sayfaBaslik,
        fotolar=fotolar
    )
    return render(request, "sayfalar/index.html", icerik)

def filmDetayView(request, filmID):
    myFilm = Filmler.objects.get(pk=filmID)
    sayfaBaslik = "Film Detay"
    icerik = dict(
        myFilm=myFilm
    )
    return render(request, "sayfalar/filmdetay.html", icerik)

def filmler(request):
    films = Filmler.objects.all()
    sayfaBaslik = "Filmler".upper()
    icerik = dict(
        sayfaBaslik=sayfaBaslik,
        films = films
    )
    return render(request, "sayfalar/filmler.html", icerik)

def tiyatro(request):
    sayfaBaslik = "Tiyatro".upper()
    icerik = dict(
        sayfaBaslik=sayfaBaslik
    )
    return render(request, "sayfalar/tiyatro.html", icerik)

def galeri(request):
    fotolar = Galeri.objects.all()
    sayfaBaslik = "Galeri".upper()
    icerik = {
        "sayfaBaslik":sayfaBaslik,
        "fotolar":fotolar
    }
    return render(request, "sayfalar/galeri.html", icerik)