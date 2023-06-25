from django.http import HttpResponse

from django.shortcuts import render , redirect
from .models import Todo
from TodoList.forms import AddTodo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
#username : admin #password : new_password123
@login_required(login_url='login')
def DisplayTodos(request):
    user = User.objects.get(username=request.user.username)
    allTodos = Todo.objects.filter(user=user)
    
    name = user.get_username()  # Retrieve the username
    context = {
        "Todos":allTodos,
        'name': name
    }
    return render(request,"display_todos.html",context)


#getting a record with pk and deleting it from the table
def DeleteTodo(request,pk):
    record = Todo.objects.get(id = pk)
    record.delete()
    return redirect('/')

def SetMark(request,pk):
    record = Todo.objects.get(id = pk)
    record.status = True
    record.save()
    return redirect('/')

def UnMark(request,pk):
    record = Todo.objects.get(id = pk)
    record.status = False
    record.save()
    return redirect('/')



def add_todo(request):
    if request.method == 'POST':
        form = AddTodo(request.POST)
        
        if form.is_valid():
            instance = Todo()
            # instance.user = form.cleaned_data['id']
            instance = form.save(commit=False)
            instance.user = request.user  # Assign the current user to the user field
            
            form.save()
            # instance.user = form.cleaned_data['user']
            return redirect('/')  # Redirect to a home page
    else:
        
        form = AddTodo()
    return render(request, 'add_todo.html', {'form': form})


def update_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    form = AddTodo(instance=todo)
    if request.method == 'POST':
        form = AddTodo(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a home page
    else:
        form = AddTodo()
    return render(request, 'update_todo.html', {'form': form})