from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

class Duyurular(models.Model):
    DuyuruBaslik = models.CharField(verbose_name = ("Duyuru Baslik"), max_length = 100)
    DuyuruIcerik = tinymce_models.HTMLField(verbose_name = ("Icerigi: "), max_length = 200)