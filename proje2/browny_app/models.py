from django.db import models

# Create your models here.


class Yazar(models.Model):
    adiSoyadi = models.CharField(verbose_name = "yazar ad", max_length= 50)
    eposta = models.EmailField(verbose_name = "e-posta adresi" , max_length = 50) 

    def __str__(self):
        return self.adiSoyadi
    
    class Meta:
        verbose_name = "yazar"
        verbose_name_plural = "yazarlar"


class Haberler(models.Model):
    baslik = models.CharField(verbose_name ="haber basligi: ", max_length=50)
    icerik = models.CharField(verbose_name = "icerik: ", max_length=50)
    tarih  = models.DateField(verbose_name = "yayin tarihi: ", auto_now=False, auto_now_add=False)
    gorsel = models.ImageField(verbose_name  ="gorsel seciniz: ")
    yazar  =  models.ForeignKey(Yazar, help_text = "seçiniz: ", 
                                   verbose_name = "Yazar seçiniz", 
                                    on_delete = models.CASCADE,
                                        blank = True, 
                                        null= True)
            
    def __str__(self):
        return self.baslik
    
    class Meta:
        verbose_name = "Haber"
        verbose_name_plural = "Haberler"




