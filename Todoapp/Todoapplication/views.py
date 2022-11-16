from django.shortcuts import render, redirect
from .models import Mytodo
from .forms import TodoForm

# Create your views here.
def Alltodo(request):
    tasks = Mytodo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'Todoapplication/index.html',{'tasks':tasks, 'form':form})

def deleteitem(request,pk):
    tasks = Mytodo.objects.get(id=pk)
    tasks.delete()
    return redirect('alltodo')

def updateitem(request, pk):
    todo = Mytodo.objects.get(id=pk)
    updateform = TodoForm(instance = todo)
    if request.method == 'POST':
        updateform = TodoForm(request.POST,instance= todo)
        if updateform.is_valid():
            updateform.save()
            return redirect('alltodo')
    return render(request,'Todoapplication/updateitem.html',{'todo':todo, 'updateform':updateform})

