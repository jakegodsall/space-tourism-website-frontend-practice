from django.shortcuts import render, redirect

from .models import Technology

# Create your views here.


def index(request):
    return redirect('vehicle')


def vehicle(request):
    vehicle = Technology.objects.get(name='launch vehicle')
    return render(request, 'technology/technology-vehicle.html', {
        'technology': vehicle
    })


def capsule(request):
    capsule = Technology.objects.get(name='space capsule')
    return render(request, 'technology/technology-capsule.html', {
        'technology': capsule
    })


def spaceport(request):
    spaceport = Technology.objects.get(name='spaceport')
    return render(request, 'technology/technology-spaceport.html', {
        'technology': spaceport
    })
