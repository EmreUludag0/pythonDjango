# user profilinin uygulamasının urlleri buradadır.

from django.urls import path
from .views import *

app_name = "user_profile" #app ismini belirtiyoruz.
# bu uygulama adını config içerisinde çağıracağız.

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register")
]
