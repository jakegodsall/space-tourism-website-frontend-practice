from django.shortcuts import render
from django.http import HttpResponse
import json

with open('data.json') as json_data:
    data = json.load(json_data)
    destinations = data['destinations']


def index(request):

    return render(request, 'destination/index.html', {
        'moon': moon,
        'mars': mars,
        'europa': europa,
        'titan': titan
    })


def europa(request):
    europa = next(d for d in destinations if d["name"] == "Europa")
    return render(request, 'destination/europa.html', {
        'destination': europa
    })


def mars(request):
    mars = next(d for d in destinations if d["name"] == "Mars")
    return render(request, 'destination/mars.html', {
        'destination': mars
    })


def moon(request):
    moon = next(d for d in destinations if d["name"] == "Moon")
    return render(request, 'destination/moon.html', {
        'destination': moon
    })


def titan(request):
    titan = next(d for d in destinations if d["name"] == "Titan")
    return render(request, 'destination/titan.html', {
        'destination': titan
    })
