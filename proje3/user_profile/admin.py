from django.contrib import admin

# Register your models here.
from .models import *

class UyelerAdmin(admin.ModelAdmin):
    list_display=[
        "user"
    ]

admin.site.register(Uyeler, UyelerAdmin)