from rest_framework import serializers
from .models import Employee,SURNAME_CHOICES,EmpTime

class ChoicesSerializerField(serializers.SerializerMethodField):
    def to_representation(self,value):
        method_name='get_{fieldName}_display'.format(fieldName=self.field_Name)
        method = getattr(value,method_name)
        return method()


class EmployeeSerializer(serializers.ModelSerializer):
    surname = serializers.ChoiceField(choices=SURNAME_CHOICES, default='Mr')
    class Meta:
        model = Employee
        fields = ['ename','empid','surname']

    '''def get_surname(self,obj):
        return obj.get_surname_display()'''
class EmpTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpTime
        fields = ['ename']

    def create(self,validated_data):
        emp,created=EmpTime.objects.create(ename=validated_data['empid'])
        return emp
