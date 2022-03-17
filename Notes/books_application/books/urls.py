from django.urls import path
from .views import create_view, list_view, detail_view, update_view, delete_view

urlpatterns = [
    path('', create_view),
    path('all_books/', list_view),
    path('book_detail/<int:id>/', detail_view),
    path('book_update/<int:id>/', update_view),
    path('book_delete/<int:id>/', delete_view),

]
