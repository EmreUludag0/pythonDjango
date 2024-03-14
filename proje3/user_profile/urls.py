from django.urls import path
from .views import *

app_name = "user_profile" 
# app ismini belirtiyoruz bu uygulamayı config içinde çağıracağız

urlpatterns = [
    path("login/", login, name="login"),
    # path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    
]
