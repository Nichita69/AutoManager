# auto/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('get_links/', views.get_links, name='get_links'),
    path('filter_autos/', views.filter_autos, name='filter_autos'),
]
