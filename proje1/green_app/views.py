from django.shortcuts import render
from datetime import datetime

sosyalMedyaHesaplari = [
    "Instagram", "linkedin", "github"
]

anasayfa_depo = {
    "konu" : "hakkimizda Sayfasi",
    "alt_konu" : "doga korunmasi",
    "konular" : [
        "doga neleri kapsar?",
        "doga ile ilgili neler yapilabilir?",
        "doga kavramlari nelerdir?",
        "doga olaylari neleri kapsar?"
    ],
    "hesaplar" : sosyalMedyaHesaplari  
}



# Create your views here.
def anasayfa(request):
    zaman = datetime.now()
    baslik = "Anasayfa"
    icerik = "Anasayfa Bulumundesiniz"
    sozluk = dict( #django kısmında kullanacagimiz kısmıları olusturdum "{{}}"
        baslik = baslik,  
        icerik = icerik,
        zaman = zaman,
        hesaplar = sosyalMedyaHesaplari
    )

    return render(request,"sayfalar/index.html", sozluk) 


def hakkimizda(request):
    return render(request, "sayfalar/hakkimizda.html", anasayfa_depo)
    
