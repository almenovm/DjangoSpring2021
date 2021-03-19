from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views
from main.views import TodoViewSet
from rest_framework import routers

router = DefaultRouter()
router.register(r'todos', viewset=views.TodoViewSet, basename='todos')

urlpatterns = [
    path('', include(router.urls))
]