from django.urls import path

from . import views

urlpatterns = [
    path('/capsule', views.capsule),
    path('/spaceport', views.spaceport),
    path('/vehicle', views.vehicle)
]
