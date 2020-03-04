from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from emp import views
urlpatterns = [
    path('list/', views.getEmployee,name='empdetail'),
    path('emplist/',views.EmployeeList.as_view(),name='emplist'),
    path('emplist/<int:pk>/',views.EmployeeDetail.as_view(),name='empdetail'),
    path('login/',views.loginlogout,name='loginlogout')
]