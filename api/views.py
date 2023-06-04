

# Create your views here.
from django.shortcuts import render
from api.serializers import Employeeserializer
from api.models import Employee
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class EmployeeView(ModelViewSet):
    model=Employee
    queryset=Employee.objects.all()
    serializer_class=Employeeserializer