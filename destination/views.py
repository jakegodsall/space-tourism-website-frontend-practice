from django.shortcuts import render
from django.http import HttpResponse
import json

with open('data.json') as json_data:
    data = json.load(json_data)
    destinations = data['destinations']


def index(request):
    moon = next(d for d in destinations if d["name"] == "Moon")
    mars = next(d for d in destinations if d["name"] == "Mars")
    europa = next(d for d in destinations if d["name"] == "Europa")
    titan = next(d for d in destinations if d["name"] == "Titan")
    return render(request, 'destination/index.html', {
        'moon': moon,
        'mars': mars,
        'europa': europa,
        'titan': titan
    })


def europa(request):
    ...


def mars(request):
    ...


def moon(request):
    ...


def titan(request):
    ...
