from django.urls import path
from . views import create_todo, list_view, delete_view,  update_view

urlpatterns=[
    path('list/', list_view),
    path('', create_todo),
    # path('detail/<int:id>/', detail_view),
    path('update/<int:id>/', update_view),
    path('delete/<int:id>', delete_view),

]

# <td>
#                 <a href="{% url 'update_view' data.id %}" class="btn btn-primary">Edit</a>
#                 <a href="{% url 'delete_view' data.id %}" class="btn btn-danger">Delete</a>
#             #   </td