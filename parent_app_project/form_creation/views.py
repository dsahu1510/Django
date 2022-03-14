from multiprocessing import context
from django.shortcuts import render

from form_creation.form import form_info
from .models import main_form
from .form import form_info
# Create your views here.

def create_view(request):
    context = {}

    form = form_info(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'create_view.html', context)