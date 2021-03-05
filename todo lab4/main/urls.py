from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.uncompleted),
    path('<int:pk>/completed/', views.completed)
]

