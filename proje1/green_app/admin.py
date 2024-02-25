from django.contrib import admin
from .models import * #models sayfasında kac tane tablo varsa getirir.

# Register your models here.

class DuyuruAdmin(admin.ModelAdmin):
    list_display = ["DuyuruBaslik","DuyuruIcerik"]

class GorselAdmin(admin.ModelAdmin):
    list_display = ["gorselBaslik"]


admin.site.register(Duyurular,DuyuruAdmin)
admin.site.register(Gorseller,GorselAdmin)  


