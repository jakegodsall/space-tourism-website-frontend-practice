from django.shortcuts import render, redirect
import json

with open('./data.json') as json_object:
    data = json.load(json_object)
    crew = data['crew']


def index(request):
    return redirect('commander')


def commander(request):
    commander = next(c for c in crew if c['role'] == 'Commander')
    return render(request, 'crew/crew-commander.html', {
        'member': commander
    })


def engineer(request):
    engineer = next(c for c in crew if c['role'] == 'Engineer')
    return render(request, 'crew/crew-engineer.html', {
        'member': engineer
    })


def pilot(request):
    pilot = next(c for c in crew if c['role'] == 'Pilot')
    return render(request, 'crew/crew-pilot.html', {
        'member': pilot
    })


def specialist(request):
    specialist = next(c for c in crew if c['role'] == 'Specialist')
    return render(request, 'crew/crew-specialist.html', {
        'member': specialist
    })
