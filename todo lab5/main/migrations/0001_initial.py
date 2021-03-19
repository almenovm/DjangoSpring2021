# Generated by Django 3.1.7 on 2021-03-05 21:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Todo List',
                'verbose_name_plural': 'Todo Lists',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(blank=True, max_length=255, null=True, verbose_name='Task')),
                ('created', models.DateField(verbose_name='Created')),
                ('due_on', models.DateField(default=datetime.datetime(2021, 3, 6, 21, 56, 50, 777016), verbose_name='Due on')),
                ('owner', models.CharField(blank=True, max_length=255, null=True, verbose_name='Owner')),
                ('mark', models.BooleanField(default=False, verbose_name='Mark')),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.todolist', verbose_name='TodoList')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['id'],
            },
        ),
    ]
