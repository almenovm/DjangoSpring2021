from django.urls import path

from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('1/completed/', views.completed_todo_list, name='completed_todo_list'),

]


