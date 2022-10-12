from django.shortcuts import render, redirect

from .models import CrewMember


def index(request):
    return redirect('commander')


def commander(request):
    commander = CrewMember.objects.get(role='Commander')
    return render(request, 'crew/crew-commander.html', {
        'member': commander
    })


def engineer(request):
    engineer = CrewMember.objects.get(role='Flight Engineer')
    return render(request, 'crew/crew-engineer.html', {
        'member': engineer
    })


def pilot(request):
    pilot = CrewMember.objects.get(role='Pilot')
    return render(request, 'crew/crew-pilot.html', {
        'member': pilot
    })


def specialist(request):
    specialist = CrewMember.objects.get(role='Mission Specialist')
    return render(request, 'crew/crew-specialist.html', {
        'member': specialist
    })
