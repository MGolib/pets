from django.db import models
import datetime

# Create your models here.

class Zakazlar(models.Model):
    ism = models.CharField(max_length=50)
    telefon = models.CharField(max_length=50)
    shahar = models.CharField(max_length=50)
    tur = models.CharField(max_length=20)
    miqdor = models.CharField(max_length=20)
    vaqt = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.ism

class Yangi(models.Model):
    itnomi = models.CharField(max_length=100)
    coment = models.TextField()
    img = models.ImageField(default='')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.itnomi

    class Meta:
        verbose_name = 'it'
        verbose_name_plural = 'Itlar'

class Yan(models.Model):
    itnomi = models.CharField(max_length=100)
    coment = models.TextField()
    img = models.ImageField(default='')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.itnomi

    class Meta:
        verbose_name = 'asosiydog'
        verbose_name_plural = 'AsosiyDogs'

class Axborot(models.Model):
    info = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = 'info'
        verbose_name_plural = 'Infos'