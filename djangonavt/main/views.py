import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    data = {
        'title' : 'Ural Statelite',
        'temperature': 1150,
        'quantity_days': 520,
        'speed': 50
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