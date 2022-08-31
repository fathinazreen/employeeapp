from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=120)
    department=models.CharField(max_length=250)
    salary=models.PositiveIntegerField()
    experience=models.CharField(max_length=120)
    email=models.CharField(max_length=250)
    def __str__(self):
        return self.name