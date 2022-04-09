from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import TodoList

# Create your views here.
class ListTodo(ListView):
    model = TodoList

class CreateTodo(CreateView):
    model = TodoList
    fields = '__all__'
    success_url = reverse_lazy('todos_list')

class UpdateTodo(UpdateView):
    model = TodoList
    fields = '__all__'
    success_url = reverse_lazy('todos_list')

class DeleteTodo(DeleteView):
    model = TodoList
    success_url = reverse_lazy('todos_list')