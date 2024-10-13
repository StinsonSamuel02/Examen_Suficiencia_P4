from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from bus.models import Bus
from employee.forms import EmployeeForm, EmployeeEditForm
from employee.models import Employee


@login_required
def employees(request):
    employees = Employee.objects.all()
    buses = Bus.objects.annotate(
        employee_count=Count('employee', distinct=True)
    ).filter(employee_count=0)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employees')
        else:
            print(form.errors)
    else:
        form = EmployeeForm()
    return render(request, 'pages/employees.html', {'form': form, 'employees': employees, 'buses': buses})


@login_required
def edit(request, id):
    employee = get_object_or_404(Employee, pk=id)
    buses = Bus.objects.annotate(
        employee_count=Count('employee', distinct=True)
    ).filter(employee_count=0)

    if request.method == 'POST':
        form = EmployeeEditForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/employees')
    else:
        form = EmployeeEditForm(instance=employee)
    return render(request, 'pages/form-edit-employee.html', {'form': form, 'employee': employee, 'buses': buses})


@login_required
def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/employees')
