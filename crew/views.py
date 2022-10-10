from django.shortcuts import render, redirect


def index(request):
    return redirect('commander')


def commander(request):
    return render(request, 'crew/crew-commander.html')


def engineer(request):
    return render(request, 'crew/crew-engineer.html')


def pilot(request):
    return render(request, 'crew/crew-pilot.html')


def specialist(request):
    return render(request, 'crew/crew-specialist.html')
