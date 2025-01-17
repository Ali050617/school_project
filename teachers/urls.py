from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [
    path('list/', views.teacher_list, name='teachers'),
    path('create/', views.teacher_create, name='create'),
    path('detail/<int:pk>/', views.teacher_detail, name='detail'),
    path('delete/<int:pk>/', views.teacher_delete, name='delete'),
]