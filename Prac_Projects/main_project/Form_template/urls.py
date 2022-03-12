from django.urls import URLPattern, path
from .views import create_view

URLPattern = [
    path('/create-book',create_view)
]