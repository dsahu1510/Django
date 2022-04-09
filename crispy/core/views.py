from django.shortcuts import render
from .forms import BasicForm, ExampleForm

# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = BasicForm()
        
    return render(request, 'signup.html', {'form':form})

def crispy_signup(request):

    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = BasicForm()

    return render(request, 'crispy_signup.html',{'form': form})

def customised_crispy_signup(request):

    if request.method =='POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = BasicForm()

    return render(request, 'customised_crispy_signup.html', {'form': form})

def crispy_helpers_signup(request):

    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ExampleForm()

    return render(request, 'crispy_helpers_signup.html', {'form': form})
