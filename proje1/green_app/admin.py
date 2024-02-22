from django.contrib import admin
from .models import * #models sayfasında kac tane tablo varsa getirir.

# Register your models here.

class DuyuruAdmin(admin.ModelAdmin):
    list_display = ["DuyuruBaslik","DuyuruIcerik"]

admin.site.register(Duyurular,DuyuruAdmin)  