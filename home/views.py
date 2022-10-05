from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    homepage = render_to_string('home/index.html')
    return HttpResponse(homepage)
