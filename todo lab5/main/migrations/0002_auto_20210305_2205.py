# Generated by Django 3.1.7 on 2021-03-05 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateField(verbose_name='Due on'),
        ),
    ]
