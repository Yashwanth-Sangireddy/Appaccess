from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee,EmpTime
from django.views.decorators.http import require_POST,require_GET
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import EmployeeSerializer,EmpTimeSerializer
from rest_framework import status
from django.http import Http404
# Create your views here.

@api_view(['GET',])
def getEmployee(request,id=None):
    if id:
        data=Employee.objects.filter(empid=id)
        serializer=EmployeeSerializer(data)
        return Response(serializer.data)
    data=Employee.objects.all()
    serializer = EmployeeSerializer(data,many=True)
    return HttpResponse(serializer.data)

class EmployeeList(APIView):
    def get(self,request,format=None):
        data=Employee.objects.all()
        serial=EmployeeSerializer(data,many=True)
        return Response(serial.data)

    def post(self,request,format=None):
        serial=EmployeeSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(empid=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        data=self.get_object(pk)
        serial=EmployeeSerializer(data)
        return Response(serial.data)
    def put(self,request,pk,format=None):
        data=self.get_object(pk)
        serial=EmployeeSerializer(data,request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        data=self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST'])
def loginlogout(request):
    if request.method == 'POST':
        empid=request.data['empid']
        empobj=Employee.objects.get(empid=empid)
        print(empobj)
        obj=EmpTimeSerializer(data=empobj)
        if obj.is_valid():
            print("%%%%%%%")
            obj.save()
        print(obj)
        return Response(obj.data)
    if request.method == 'GET':
        return Response("Hellllo")