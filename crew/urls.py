from django.urls import path

from . import views

urlpatterns = [
    path('/commander', views.commander),
    path('/engineer', views.engineer),
    path('/pilot', views.pilot),
    path('specialist', views.specialist)
]
