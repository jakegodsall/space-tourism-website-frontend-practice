from django.http import HttpResponse
from django.template.loader import render_to_string


def index(response):
    homepage = render_to_string('home/index.html')
    return HttpResponse(homepage)
