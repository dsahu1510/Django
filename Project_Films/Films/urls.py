from django.urls import path

from . import views

urlpatterns = [
    path('films/film_list', views.FilmListView.as_view(), name = 'film_list'),
    path('films/<int:pk>/update/', views.FilmUpdateView.as_view(), name = 'film_update'),
    path('films/<int:pk>/delete/', views.FilmDeleteView.as_view(), name = 'film_delete'),
    path('', views.FilmCreateView.as_view(), name = 'film_create')
]