from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('vehicle', views.vehicle, name='vehicle'),
    path('capsule', views.capsule, name='capsule'),
    path('spaceport', views.spaceport, name='spaceport'),
]
