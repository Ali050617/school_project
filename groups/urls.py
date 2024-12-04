from django.urls import path
from . import views


app_name = 'groups'

urlpatterns = [
    path('group/', views.group_list, name='groups'),
    path('create/', views.group_create, name='create'),
    path('detail/<int:pk>/', views.group_delete, name='detail'),
    path('delete/<int:pk>/', views.group_delete, name='delete'),
]