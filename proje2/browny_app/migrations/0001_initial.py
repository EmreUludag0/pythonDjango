# Generated by Django 5.0.2 on 2024-02-29 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yazar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adiSoyadi', models.CharField(max_length=50, verbose_name='yazar ad')),
                ('eposta', models.EmailField(max_length=50, verbose_name='e-posta adresi')),
            ],
        ),
        migrations.CreateModel(
            name='Haberler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50, verbose_name='haber basligi: ')),
                ('icerik', models.CharField(max_length=50, verbose_name='icerik: ')),
                ('tarih', models.DateField(verbose_name='yayin tarihi: ')),
                ('gorsel', models.ImageField(upload_to='', verbose_name='gorsel seciniz: ')),
                ('yazar', models.OneToOneField(blank=True, help_text='seçiniz: ', null=True, on_delete=django.db.models.deletion.CASCADE, to='browny_app.yazar', verbose_name='Yazar seçiniz')),
            ],
            options={
                'verbose_name': 'Haber',
                'verbose_name_plural': 'Haberler',
            },
        ),
    ]
