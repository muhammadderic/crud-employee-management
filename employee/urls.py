from django.urls import path
from .views import create_employee, employee_list

urlpatterns = [
  path('', employee_list, name="list"),
  path('create/', create_employee, name='create'),
]