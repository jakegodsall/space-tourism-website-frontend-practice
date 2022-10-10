from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
import json

with open('data.json') as json_data:
    data = json.load(json_data)
    destinations = data['destinations']


def index(request):
    return redirect('europa')


def europa(request):
    europa = next(d for d in destinations if d["name"] == "Europa")
    return render(request, 'destination/destination-europa.html', {
        'destination': europa
    })


def mars(request):
    mars = next(d for d in destinations if d["name"] == "Mars")
    return render(request, 'destination/destination-mars.html', {
        'destination': mars
    })


def moon(request):
    moon = next(d for d in destinations if d["name"] == "Moon")
    return render(request, 'destination/destination-moon.html', {
        'destination': moon
    })


def titan(request):
    titan = next(d for d in destinations if d["name"] == "Titan")
    return render(request, 'destination/destination-titan.html', {
        'destination': titan
    })
