from django.db import models

# Create your models here.
class Uyeler(models.Model):
    eposta = models.EmailField(verbose_name="E-Posta Adresi", max_length=100)
    parola = models.CharField(verbose_name="Parola", max_length=50)
    adi = models.CharField(verbose_name="Adi", max_length=50)
    soyadi = models.CharField(verbose_name="Soyadi", max_length=50)
    kullaniciFoto = models.ImageField(verbose_name="Kullanıcı Fotoğrafı")
    
    class Meta:
        verbose_name="Üye"
        verbose_name_plural = "Üyeler"
    
    def __str__(self):
        return self.eposta
    