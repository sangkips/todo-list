from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.loginView, name='logout'),
    path('register/', views.registerView, name='register'),

    path('', views.index, name='home'),

    path('create/', views.createTodo, name='create'),
    path('edit/<str:pk>/', views.editTodo, name='edit'),
    path('delete/<str:pk>/', views.deleteTodo, name='delete'),
]
