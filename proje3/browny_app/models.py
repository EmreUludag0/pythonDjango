from django.db import models

class Kurslar(models.Model):
    pass

class Alanlar(models.Model):
    pass

class Programlar(models.Model):
    pass

class Programlar(models.Model):
    turu =  [
        ("1", "yuzyuze Egitim"),
        ("2", "Uzaktan egitim"),
        ("3", "harmanlanmiş egitim"),
    ]
    sertifika = [
        ("1", "sertifika"), 
        ("2", "katilim belgesi"),
        ("3", "meb onayli sertifika")
    ]

    isim = models.CharField(verbose_name = "Program Adi: ", max_length = 100)
    amaci = models.TextField(verbose_name = "Programın amaci: ")
    egitimTuru = models.CharField(verbose_name  = "egitim Turu", choices = turu, max_length = 50)
    sertifikadurumu = models.CharField(choices = sertifika, verbose_name= "sertifika turu", max_length = 50)


class Yazar(models.Model):
    adiSoyadi = models.CharField(verbose_name="Yazar Adı:", max_length=50)
    eposta = models.EmailField(verbose_name="E-Posta Adresi:", max_length=254)
    
    def __str__(self):
        return self.adiSoyadi
    
    class Meta:
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar" 
    
# Create your models here.
class Haberler(models.Model):
    baslik = models.CharField(verbose_name="Haber Başlığı:", max_length=50)
    icerik = models.CharField(verbose_name="İçerik:", max_length=50)
    tarih = models.DateField(verbose_name="Yayın Tarihi:", auto_now=False, auto_now_add=False)
    gorsel = models.ImageField(verbose_name="Görsel Seçiniz:")
    yazar = models.ForeignKey(Yazar, help_text="Seçiniz.", 
                                verbose_name="Yazar Seçiniz", 
                                on_delete = models.CASCADE, 
                                blank=True, null=True)
    def __str__(self):
        return self.baslik
    
    class Meta:
        verbose_name = "Haber"
        verbose_name_plural = "Haberler"
    