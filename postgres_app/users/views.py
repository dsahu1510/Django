from django.shortcuts import render
from .models import User, Company

# Create your views here.
def display(request, pk):
    user = User.objects.get(pk = pk)
    Company_detail = Company.objects.get()

    context = {
        "users": user,
        "company":Company
    }

    return render(request, 'user_detail.html',context)

    