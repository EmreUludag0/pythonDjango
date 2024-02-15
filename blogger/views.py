# views, sayfaların ilgili mettotlarını / fonksiyonlarının tanımlamalarını buraya yaparız. (Tanımlama)
# sayfaların link / baglanti tanımlamasını config > urls.py dosyasında yapıyoruz. (Cagirma)
from django.shortcuts import render

# Create your views here.

def anasayfa(request):
    sayfaBaslik = "Ana Sayfa".upper()
    icerik = "Python Django Projesi"
    bilgiler  = dict(
        sayfaBaslik = sayfaBaslik,
        icerik = icerik
    )

    return render(request,"sayfalar\index.html", bilgiler)
