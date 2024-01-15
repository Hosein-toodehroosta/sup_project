from django.db import models

# Create your models here.

class CustomerModel(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام مشتری')
    shenaseh_melli = models.CharField(max_length=20, verbose_name='شناسه ملی')
    shomareh_sabt = models.CharField(max_length=20, verbose_name='شماره ثبت')
    tarikh_sabt = models.CharField(max_length=20, verbose_name='تاریخ ثبت')
    address = models.CharField(max_length=500, verbose_name='آدرس')
