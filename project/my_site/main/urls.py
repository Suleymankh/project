from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.epoch1),
    path('', views.epoch2),
    path('', views.epoch3),
    path('', views.epoch4),
    path('', views.collection1),
    path('', views.collection2),
    path('', views.collection3),
    path('', views.collection4),
]
