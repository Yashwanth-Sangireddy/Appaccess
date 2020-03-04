from django.contrib import admin
from .models import Employee,EmpTime
class EmployeeAdmin(admin.ModelAdmin):
    fields=['surname','ename','empid','empdetails']


# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(EmpTime)