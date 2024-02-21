from django.shortcuts import render
from datetime import datetime

# Create your views here.
def anasayfa(request):
    zaman = datetime.now()
    baslik = "Anasayfa"
    icerik = "Anasayfa Bulumundesiniz"
    sozluk = dict( #django kısmında kullanacagimiz kısmıları olusturdum "{{}}"
        baslik = baslik,  
        icerik = icerik,
        zaman = zaman
    )

    return render(request,"sayfalar/index.html", sozluk) 
