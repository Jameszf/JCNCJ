
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.index),
    path('path/', views.play),
    path('profile/', views.profile),
    path('create/', views.create),
]
