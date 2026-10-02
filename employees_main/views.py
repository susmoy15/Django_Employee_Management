from django.http import HttpResponse
from employees.models import Employee
from django.shortcuts import render

# Decided which URL pattern to create
# Created URL pattern in the main urls.py, and forward it to employees.urls
# Created the view
# Created the template

def home(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render (request, 'home.html', context)   


