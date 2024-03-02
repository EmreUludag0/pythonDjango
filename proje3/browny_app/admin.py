from django.contrib import admin
from .models import *

# Register your models here.
class HaberlerAdmin(admin.ModelAdmin):
    list_display = [
        "baslik", "tarih"
    ]

admin.site.register(Yazar)
admin.site.register(Haberler, HaberlerAdmin)