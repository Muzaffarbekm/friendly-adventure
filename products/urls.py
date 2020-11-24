from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),  # '' means route url  views.index is function 
    path('new', views.new)
]