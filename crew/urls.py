from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='crew'),
    path('commander', views.commander, name='commander'),
    path('engineer', views.engineer, name='engineer'),
    path('pilot', views.pilot, name='pilot'),
    path('specialist', views.specialist, name='specialist')
]
