from django.shortcuts import render

from employee.models import Employee
from .forms import EmployeeForm
from django.shortcuts import redirect
# from django.http import HttpResponse
# Create your views here.

# def Home(request):
#     return render(request, 'home.html')

#create view
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm()
    return render(request, 'create.html',{'form':form})

#list view

def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'list.html', {'employees':employee})

# update view

def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html',{'form':form})

# delete view

def delete_employee(request,pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
    return redirect('list')


