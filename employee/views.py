from django.shortcuts import render
from .models import Employee

def employee_list(request):
    """
    View to list all Employee model instances.

    :param request: The request object
    :return: The rendered template
    """
    employee = Employee.objects.all()
    return render(request, 'list.html', {'employees':employee})
