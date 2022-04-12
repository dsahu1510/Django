from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def create_todo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list')

    context = {'form': form}
    return render(request, 'create_todo.html', context)

def list_view(request):
    context = Todo.objects.all()
    return render(request, 'list.html', {'context' : context})

# def detail_view(request, id):

#     context['data'] = Todo.objects.get(id = id)
#     return render(request, 'detail_view.html', context)

def update_view(request, id):
    obj = get_object_or_404(Todo, id = id)
    form = TodoForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/list')

    context = {'form': form}
    return render(request, 'update_view.html', context)

def delete_view(request, id):
    obj = get_object_or_404(Todo, id = id)

    if request.method == 'POST':
        obj.delete()
        return redirect('/list')
    context = {'todo': obj}
    return render (request, 'delete_view.html', context)
