from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='destination'),
    path('europa', views.europa, name='europa'),
    path('mars', views.mars, name='mars'),
    path('moon', views.moon, name='moon'),
    path('titan', views.titan, name='titan')
]
