from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'destination/index.html')


def europa(request):
    ...


def mars(request):
    ...


def moon(request):
    ...


def titan(request):
    ...
