from django.shortcuts import redirect, render

from .models import Destination


def index(request):
    return redirect('europa')


def europa(request):
    europa = Destination.objects.get(name='europa')
    return render(request, 'destination/destination-europa.html', {
        'destination': europa
    })


def mars(request):
    mars = Destination.objects.get(name='mars')
    return render(request, 'destination/destination-mars.html', {
        'destination': mars
    })


def moon(request):
    moon = Destination.objects.get(name='moon')
    return render(request, 'destination/destination-moon.html', {
        'destination': moon
    })


def titan(request):
    titan = Destination.objects.get(name='titan')
    return render(request, 'destination/destination-titan.html', {
        'destination': titan
    })
