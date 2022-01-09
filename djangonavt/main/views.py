from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    data = {
        'title' : 'Ural Statelite',
        'temperature': 1150,
        'quantity_days': 520,
        'speed': 50,
        'amperage_k': 10,
        'amperage_n': 10,
        'pressure': 16,
        'voltage': 20,
        'traction': 10
    }
    return render(request, 'main/index.html', data) #передаем значения

def start(request):
    print("fuck")
    data = {
        'title' : 'Ural Statelite',
        'temperature': 11500,
        'quantity_days': 5200,
        'speed': 500
    }
    return render(request, 'main/index.html', data)