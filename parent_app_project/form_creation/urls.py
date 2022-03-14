from django.urls import path
from .views import create_view  

urlpattern = [
    path('', create_view)
]