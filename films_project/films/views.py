from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Film
# Create your views here.

class FilmListView(ListView):
    model = Film

class FilmCreateView(CreateView):
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('films_list')

class FilmUpdateView(UpdateView):
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('films_list')

class FilmDeleteView(DeleteView):
    model = Film
    success_url = reverse_lazy('films_list')

