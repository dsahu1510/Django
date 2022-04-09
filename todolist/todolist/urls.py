"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todo.views import CreateTodo, ListTodo, UpdateTodo, DeleteTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',CreateTodo.as_view(), name = 'todos_create'),
    path('todos/list_view',ListTodo.as_view(), name = 'todos_list'),
    path('todos/<int:pk>/update',UpdateTodo.as_view(), name = 'todos_update'),
    path('todos/<int:pk>/delete',DeleteTodo.as_view(), name = 'todos_delete'),
]
