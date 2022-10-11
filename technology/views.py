from django.shortcuts import render, redirect
import json

# Create your views here.

with open('data.json', 'r') as json_object:
    data = json.load(json_object)
    technology = data['technology']


def index(request):
    return redirect('vehicle')


def vehicle(request):
    vehicle = next(t for t in technology if t['name'] == 'Launch vehicle')
    return render(request, 'technology/technology-vehicle.html' {
        'tech': vehicle
    })


def capsule(request):
    capsule = next(t for t in technology if t['name'] == 'Space capsule')
    return render(request, 'technology/technology-capsule.html' {
        'tech': capsule
    })


def spaceport(request):
    spaceport = next(t for t in technology if t['name'] == 'Spaceport')
    return render(request, 'technology/technology-spaceport.html' {
        'tech': spaceport
    })
