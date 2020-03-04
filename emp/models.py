from django.db import models
import datetime

SURNAME_CHOICES=(
    ("Mr","Mr"),
    ("Mrs","Mrs")
)
# Create your models here.
class Employee(models.Model):
    surname = models.CharField(max_length=10,choices=SURNAME_CHOICES,default='Mr')
    ename = models.CharField(max_length=30,blank=False)
    empid=models.IntegerField(primary_key=True,blank=False,unique=True)
    empdetails=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.ename

class EmpTime(models.Model):
    ename=models.ForeignKey(Employee,on_delete=models.CASCADE)
    checkin=models.DateTimeField()
    checkout=models.DateTimeField()

    def __str__(self):
        return self.ename