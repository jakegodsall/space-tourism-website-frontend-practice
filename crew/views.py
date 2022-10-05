from django.shortcuts import render


def index(request):
    return render(request, 'crew/index.html')


def commander(request):
    ...


def engineer(request):
    ...


def pilot(request):
    ...


def specialist(request):
    ...
