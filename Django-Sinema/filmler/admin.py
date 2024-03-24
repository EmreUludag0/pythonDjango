from django.contrib import admin
from .models import *


# Register your models here.
class FilmlerAdmin(admin.ModelAdmin):
    list_display = [
        "baslik",
        "gosterimdeMi"
    ]


class YonetmenAdmin(admin.ModelAdmin):
    list_display = [
        "adiSoyadi"
    ]

admin.site.register(Oyuncular)
admin.site.register(Galeri)
admin.site.register(Filmler, FilmlerAdmin)
admin.site.register(Yonetmen, YonetmenAdmin)