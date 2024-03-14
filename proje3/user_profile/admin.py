from django.contrib import admin
from .models import *
# Register your models here.

class UyelerAdmin(admin.ModelAdmin):
    list_display = [
        "user"
    ]


admin.site.register(Uyeler, UyelerAdmin)