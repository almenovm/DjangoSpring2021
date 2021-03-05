from django.shortcuts import render
from .models import TodoList, Task


def completed(request, pk):
    todo = TodoList.objects.get(id=pk)
    tasks = Task.objects.filter(todo_list__id=pk, mark=True)
    context = {
        'todo': todo,
        'tasks': tasks
    }
    return render(request, 'completed_todo_list.html', context)


def uncompleted(request, pk):
    todo = TodoList.objects.get(id=pk)
    tasks = Task.objects.filter(todo_list__id=pk, mark=False)
    context = {
        'todo': todo,
        'tasks': tasks
    }
    return render(request, 'todo_list.html', context=context)
