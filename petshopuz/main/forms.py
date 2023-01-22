from django.forms import ModelForm

from .models import Zakazlar


class ZakazForm(ModelForm):
    class Meta:
        model = Zakazlar
        fields = ['ism', 'telefon', 'shahar','tur', 'miqdor']

