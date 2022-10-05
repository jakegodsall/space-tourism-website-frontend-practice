from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='technology'),
    path('capsule', views.capsule),
    path('spaceport', views.spaceport),
    path('vehicle', views.vehicle)
]
