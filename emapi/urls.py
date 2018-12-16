from django.urls import path
from . import views

urlpatterns = [ 
        path('employees/',views.index,name='index'),
        path('addemployee/',views.post,name='post'),
        path('employee/<int:employee_id>/',views.list,name='list'),
        ]
