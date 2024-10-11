from django.urls import path
from .views import pesel_view

urlpatterns = [
    path('', pesel_view, name='pesel_view'),
]