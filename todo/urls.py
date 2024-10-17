from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/', views.CreateTodoView.as_view(), name='create'),
    path('detail/<int:pk>/', views.DetailTodoView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.EditTodoView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.DeleteTodoView.as_view(), name='delete'),
]