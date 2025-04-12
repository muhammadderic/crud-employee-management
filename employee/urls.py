from django.urls import path
from .views import create_employee, delete_employee, employee_list, update_employee

urlpatterns = [
  path('', employee_list, name="list"),
  path('create/', create_employee, name='create'),
  path('update/<int:pk>/', update_employee, name="update"),
  path('delete/<int:pk>/', delete_employee, name="delete"),
]