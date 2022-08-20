from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

def index(request):
    q = request.GET.get('q',None)
    items = ''
    if q is None or q is "":
        employee = Employee.objects.all()
    elif q is not None:
        employee = Employee.objects.filter(eid__contains=q)

# Create your views here.
def createemp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})

def showemp(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {'employees':employees})

def editemp(request, id):
    employee = Employee.objects.get(id = id)
    return render(request, 'edit.html', {'employee': employee})

def updateemp(request, id):
    employee = Employee.objects.get(id= id)
    form = EmployeeForm(request.POST, instance= employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'employee':employee})

def deleteemp(request, id):
    employee = Employee.objects.get(id = id)
    employee.delete()
    return redirect ('/show')

# # def search_function(request, id):
#     	search = request.GET.get('search')
#     	q = Model.objects.filter(fieldname=search)
#     	return render(request, 'index.html', {'q':q})

    
