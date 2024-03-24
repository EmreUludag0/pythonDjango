
from django.urls import path, include
from user_profile.views import *   # views içinde tüm fonks. getir

# media dosyaları kullanmak için ekledik
from django.conf import settings
from django.conf.urls.static import static

app_name = "user_profile"

urlpatterns = [
    path('login/', loginView, name="loginView"),
    path('logout/', logoutView, name="logoutView"),
    path('register/', registerView, name="registerView"),
    path('profilim/', profilView, name="profilView"),
    path('tinymce/', include('tinymce.urls')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)