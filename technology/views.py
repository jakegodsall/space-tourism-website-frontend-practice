from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'technology/index.html')


def capsule(request):
    ...


def spaceport(request):
    ...


def vehicle(request):
    ...
