from django.urls import path
from .views import asosiyfun, ikkinchi, uchinchi, asosiy, zakas, asosiy2

urlpatterns = [
    path('', asosiyfun, name='main'),
    path('second', ikkinchi, name='ikkinchi'),
    path('third', uchinchi, name='uchinchi'),
    path('asosiy', asosiy, name='asosiy'),
    path('buyurtma', zakas, name='zakas'),
    path('asosiy2', asosiy2, name='asosiy2')
]
