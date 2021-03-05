from django.contrib import admin
from main.models import TodoList, Task


# Register your models here.

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'created', 'due_on', 'owner', 'mark', 'todo_list']
    ordering = ['id']
    search_fields = ['task', 'owner']
    list_filter = ['created', 'due_on', 'owner', 'mark']
