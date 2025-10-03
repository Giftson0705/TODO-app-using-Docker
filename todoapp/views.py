from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Todo

# Home Page showing todos
@login_required
def home(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, "home.html", {"todos": todos})

# User Registration
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created! You can now login.")
        return redirect("login")

    return render(request, "register.html")

# User Login
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")

# User Logout
def logout_view(request):
    logout(request)
    return redirect("login")

# Add Todo
@login_required
def add_todo(request):
    if request.method == "POST":
        task = request.POST["task"]
        Todo.objects.create(user=request.user, task=task)
        return redirect("home")
    return render(request, "add_todo.html")

# Delete Todo
@login_required
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.delete()
    return redirect("home")

@login_required
def edit_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    if request.method == "POST":
        todo.task = request.POST["task"]
        todo.save()
        return redirect("home")
    return render(request, "edit_todo.html", {"todo": todo})