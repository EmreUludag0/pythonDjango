from django.db import models
from tinymce import models as tinymce_models


class Galeri(models.Model):
    baslik = models.CharField(verbose_name="Görsel Başlık", max_length=100)
    image = models.ImageField(verbose_name="Fotoğraf Seçin")

    def __str__(self):
        return self.baslik
    class Meta:
        verbose_name = "Galeri"
        verbose_name_plural = "Galeriler"
    

class Yonetmen(models.Model):
    adiSoyadi = models.CharField(verbose_name=("Yönetmen Ad Soyad"), max_length=50)
    eposta = models.CharField(verbose_name=("Eposta Adresi"), max_length=50)

    def __str__(self):
        return self.adiSoyadi
    
    class Meta:
        verbose_name="Yönetmen"
        verbose_name_plural = "Yönetmenler"

class Oyuncular(models.Model):
    adsoyad =  models.CharField(max_length=64, verbose_name='Ad Soyad')
    
    def __str__(self):
        return self.adsoyad
    
    class Meta:
        verbose_name="Oyuncu"
        verbose_name_plural = "Oyuncular"
    

class Filmler(models.Model):
    
    baslik=models.CharField(verbose_name=("Film Başlığı"), max_length=100)
    turu = models.CharField(verbose_name=("Film Türü"), max_length=50)
    image = models.ImageField(verbose_name="Film Afişi")
    konu = tinymce_models.HTMLField(verbose_name=("Film Konusu"), blank=True, null=True)
    gosterimdeMi = models.BooleanField(verbose_name=("Gösterimde Mi:"), default=True)
    gosterimTarihi=models.DateTimeField(verbose_name=("Gösterim Tarihi"), auto_now=False, auto_now_add=False)
    oyuncu=models.ManyToManyField(Oyuncular, verbose_name="Oyuncu Seçin")
    filmAfis = models.CharField(verbose_name=("Film Başlığı"), max_length=100)
    biletFiyat = models.FloatField(verbose_name=("Bilet Fiyat"), blank=True, null=True)
    director = models.OneToOneField(Yonetmen, verbose_name=("Yonetmen Bilgisi"), on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name="Film"
        verbose_name_plural = "Filmler"    
    
    def __str__(self):
        return self.baslik