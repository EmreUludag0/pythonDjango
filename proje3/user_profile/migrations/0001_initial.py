# Generated by Django 5.0.2 on 2024-03-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uyeler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=50, verbose_name='Adı')),
                ('soyadi', models.CharField(max_length=50, verbose_name='Soyadı')),
                ('eposta', models.CharField(max_length=150, verbose_name='Mail Adresi')),
                ('parola', models.CharField(max_length=50, verbose_name='Parola')),
                ('kullaniciFoto', models.ImageField(upload_to='', verbose_name='kullanıcı avaratı')),
            ],
            options={
                'verbose_name': 'Üye',
                'verbose_name_plural': 'Üyeler',
            },
        ),
    ]
