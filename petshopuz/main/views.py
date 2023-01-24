from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse
from .forms import ZakazForm
from .models import Yangi, Zakazlar, Axborot, Yan

# Create your views here.

def asosiyfun(request):
    new = Yangi.objects.all()
    context = {
        'new' : new
    }
    return render(request, 'main/index.html', context)

def ikkinchi(request):

    return render(request, 'main/2.html')

def uchinchi(request):

    return render(request, 'main/3.html')

def asosiy(request):
    information = Axborot.objects.all()
    context = {
        'information' : information
    }
    return render(request, 'main/Asosiy.html', context)
def asosiy2(request):
    info = Yan.objects.all()
    context2 = {
        'info' : info
    }
    return render(request, 'main/Asosiy.html', context2)

def zakas(request):
    if request.method == 'POST':
        form = ZakazForm(request.POST)
        if form.is_valid():
            form.save()
            print("saqlandi")
            return redirect('zakas')
        else:
            print("Xatolik buldi")

    return render(request, 'main/Zakas.html')

# test uchun