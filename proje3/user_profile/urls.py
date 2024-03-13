from django.urls import path
from .views import *

app_name = "user_profile" #app ismini belirtiyoruz, bu uygulamayı config  içinde çagiracagiz

urlpatterns = [
    path("login/", loagin, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register")
]

