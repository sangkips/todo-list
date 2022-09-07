from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from . import forms
from .models import Todo
from .forms import TodoForm, LoginForm, CreateFormUser


def loginView(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            username=username,
            password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'app/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('login')


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'app/index.html', context)


def registerView(request):
    form = CreateFormUser

    if request.method == 'POST':
        form = CreateFormUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'app/register.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def deleteTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    context = {
        'todo': todo
    }

    return render(request, 'app/delete.html', context)
