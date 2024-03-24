from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Kullanıcı Adı", on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name="Kullanıcı Gorseli", upload_to="avatar")
    slug = AutoSlugField(
        unique_with=["user__first_name", "user__last_name"],
    )
