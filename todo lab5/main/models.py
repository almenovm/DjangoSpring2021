from django.db import models
import datetime


# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Name')

    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'


class Task(models.Model):
    task = models.CharField(max_length=255, null=True, blank=True, verbose_name='Task')
    created = models.DateField(verbose_name='Created')
    due_on = models.DateField(verbose_name='Due on')
    owner = models.CharField(max_length=255, null=True, blank=True, verbose_name='Owner')
    mark = models.BooleanField(default=False, verbose_name='Mark')
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='tasks', verbose_name='TodoList')

    class Meta:
        ordering = ['id']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
