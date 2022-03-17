from django.urls import path
from .views import create_form, delete_view, detail_view, list_view, update_view

urlpatterns = [
    path('',create_form),
    path('books_list/', list_view),
    path('book_detail/<int:id>/', detail_view),
    path('book_update/<int:id>/', update_view),
    path('book_del/<int:id>/', delete_view)
]