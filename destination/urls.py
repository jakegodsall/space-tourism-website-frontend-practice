from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='destination'),
    path('/europa', views.europa),
    path('/mars', views.mars),
    path('/moon', views.moon),
    path('/titan', views.titan)
]
