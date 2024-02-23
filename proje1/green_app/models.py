from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

class Duyurular(models.Model):
    DuyuruBaslik = models.CharField(verbose_name = ("Duyuru Baslik"), max_length = 100)
    DuyuruIcerik = tinymce_models.HTMLField(verbose_name = ("Icerigi: "), max_length = 200)

    class Meta:
        verbose_name = "Duyurular"
        verbose_name_plural = "Duyurular"

class Gorseller(models.Model):
    gorselBaslik = models.CharField(verbose_name = ("Gorsel Basligi: "), max_length = 100)
    image = models.ImageField(verbose_name=("Galeri Gorseli: "))

    class Meta:
        verbose_name = "gorsel"
        verbose_name_plural = "gorseller"
        