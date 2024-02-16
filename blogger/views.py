# views, sayfaların ilgili mettotlarını / fonksiyonlarının tanımlamalarını buraya yaparız. (Tanımlama)
# sayfaların link / baglanti tanımlamasını config > urls.py dosyasında yapıyoruz. (Cagirma)
from django.shortcuts import render

# Create your views here.

def Anasayfa(request):
    sayfaBaslik = "Ana Sayfa".upper()
    icerik = "Python Django Projesi"
    bilgiler  = dict(
        sayfaBaslik = sayfaBaslik,
        icerik = icerik
    )

    return render(request,"sayfalar\index.html", bilgiler)

def Blog(request):
    sayfaBaslik = "Blog".upper()
    icerik = "Icerik Sayfasina hosgeldiniz"
    bilgiler = dict(
        sayfaBaslik = sayfaBaslik,
        icerik = icerik
    )

    return render(request, "sayfalar\blog.html", bilgiler)

def Hakkimizda(request):
    sayfaBaslik = "Hakkimizda".upper()
    icerik = "Icerik Sayfasina hosgeldiniz"
    bilgiler = dict(
        sayfaBaslik = sayfaBaslik,
        icerik = icerik
    )

    return render(request, "sayfalar\hakkimizda.html", bilgiler)

def Iletisim(request):
    sayfaBaslik = "Iletisim".upper()
    icerik = "Icerik Sayfasina hosgeldiniz"
    bilgiler = dict(
        sayfaBaslik = sayfaBaslik,
        icerik = icerik
    )

    return render(request, "sayfalar\iletisim.html", bilgiler)

