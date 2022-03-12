from multiprocessing import context
from django.shortcuts import render
from . models import newBooks
from . forms import bookForm

# Create your views here.
#logic for creating a view we have to come to views.py

def create_view(request): #function created with a name
    #context passing which is an empty dictionary

    context = {} #add dictionary during initialization

    form = bookForm(request.POST or None) # here we need to use requst nd post method must be used if not post thn none must be there.
    if form.is_valid(): #validating the form and saving it
        form.save()

    context['form'] = form #form which is being saved from request.post is being written here.

    return render(request, "create_view.html", context) #returning a html page, one frontend pge must be displayed
    
