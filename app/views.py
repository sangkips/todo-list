from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from . import forms
from .models import Todo
from .forms import TodoForm, LoginForm


def loginView(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #form = LoginForm(request.POST)
        #if form.is_valid():
        user = authenticate(
            username=username,
            password=password)
        if user is not None:
            login(request, user)
            message = f'Hello {user.username}! You have been logged in'
            return redirect('home')
        else:
            message = f'Username or Password is incorrect'
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'app/login.html', context)


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'app/index.html', context)


def createTodo(request):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'app/create.html', context)


def editTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'app/edit.html', context)


def deleteTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    context = {
        'todo': todo
    }

    return render(request, 'app/delete.html', context)
