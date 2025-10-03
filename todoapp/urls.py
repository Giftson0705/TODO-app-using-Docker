from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Homepage
    path("register/", views.register, name="register"),  # User signup
    path("login/", views.login_view, name="login"),  # User login
    path("logout/", views.logout_view, name="logout"),  # User logout
    path("add/", views.add_todo, name="add_todo"),  # Add todo
    path("delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),  # Delete todo
    path("edit/<int:todo_id>/", views.edit_todo, name="edit_todo"),
]
