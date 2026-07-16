from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# The router automatically generates the CRUD URL patterns
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]