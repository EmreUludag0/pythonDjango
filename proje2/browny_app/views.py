from django.shortcuts import render


# Create your views here.

def anasayfa(request):
    baslik = "Anasayfa"
    sozluk = dict(
        baslik = baslik
    )

    return render(request, "sayfalar/index.html", sozluk)


















