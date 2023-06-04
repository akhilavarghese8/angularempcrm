from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()

    def __str__(self):
        return self.name

