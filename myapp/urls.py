from django.urls import path
from . import views
# from .views import task_list

urlpatterns = [
    path('task_list/', views.task_list, name='task_list'),
    path('task_create/', views.task_create, name='task_create'),
    path('task/<int:id>/', views.task_detail, name='task_detail'),
    path('task/<int:id>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:id>/edit/', views.task_edit, name='task_edit'),
]
