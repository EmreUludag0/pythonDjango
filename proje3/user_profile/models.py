from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Uyeler(models.Model):
    user = models.OneToOneField(User, verbose_name="Kullanıcı Adı", on_delete=models.CASCADE,null=True)
    adi = models.CharField(verbose_name="Adı", max_length=50)
    soyadi = models.CharField(verbose_name="Soyadı", max_length=50)
    eposta = models.CharField(verbose_name="Mail Adresi", max_length=150)
    parola = models.CharField(verbose_name="Parola", max_length=50)
    kullaniciFoto = models.ImageField(verbose_name="kullanıcı avaratı")
    class Meta:
        verbose_name = "Üye"
        verbose_name_plural = "Üyeler"

        def __str__(self):
            return self.kullaniciadi
