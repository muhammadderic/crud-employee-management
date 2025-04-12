from django.shortcuts import redirect, render

from .forms import EmployeeForm
from .models import Employee

def create_employee(request):
    """
    View to create new Employee model instance.

    If the request is a POST, validates the form and if valid, saves the form and redirects
    to the list view. If the request is a GET, renders an empty form.

    :param request: The request object
    :return: The rendered template
    """
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm() 
    return render(request, 'create.html', {'form':form})

def employee_list(request):
    """
    View to list all Employee model instances.

    :param request: The request object
    :return: The rendered template
    """
    employee = Employee.objects.all()
    return render(request, 'list.html', {'employees':employee})

def update_employee(request, pk):
    """
    View to update an existing Employee model instance.

    Retrieves the employee instance by primary key (pk). If the request is a POST,
    validates the form and if valid, updates the employee instance and redirects
    to the list view. If the request is a GET, renders the form with the current
    employee details.

    :param request: The request object
    :param pk: The primary key of the Employee to update
    :return: The rendered template
    """
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form':form})