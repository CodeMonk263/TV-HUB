from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ),
    path('show', views.index),
    path('season', views.index),
    path('episode', views.index)
]