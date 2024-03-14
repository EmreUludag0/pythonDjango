from django.contrib import admin
from .models import *
# Register your models here.

class UyelerAdmin(admin.ModelAdmin):
    list_display = [
        "eposta", "adi", "soyadi"
    ]


admin.site.register(Uyeler, UyelerAdmin)