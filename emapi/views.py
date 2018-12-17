from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import employee
from django.core import serializers
import json
import emapi

def index(request):
    response_data={}
    posts=employee.objects.all()
    for e in posts.iterator():
        post_data=e.get_dict()
        response_data[e.employee_id]=post_data
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def list(request, employee_id):
    emp_id=int(str(employee_id).split('/')[-1])
    try:
        posts=employee.objects.get(employee_id=emp_id)
    except: 
        response_body={ 'status code': 404,
                'body': 'Employee id: '+str(employee_id)+' not found',
                }
        return HttpResponseNotFound(json.dumps(response_body),content_type="application/json")
    context={
        str(employee_id):{
            'employee_id':posts.employee_id,
            'first_name':posts.first_name,
            'last_name':posts.last_name,
            'department': posts.department,
            }
        }
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def post(request):
    if request.method=="PUT":
        json_data=json.loads(str(request.body,encoding='utf-8'))
        for k,v in json_data.items():
            try:
                getobj=employee.objects.get(employee_id=int(v['employee_id']))
            except emapi.models.employee.DoesNotExist:
                getobj=None
            if getobj is not None:
                response_body={ 'status code': 404,
                     'body': 'DUPLICATE DATA',
                    }
                return HttpResponseNotFound(json.dumps(response_body),content_type="application/json")    
            if 1 <= int(v['employee_id']) <= 100 :
                obj=employee(employee_id=v['employee_id'],first_name=v['first_name'],last_name=v['last_name'],department=v['department'])
                obj.save()
                return HttpResponse(request.body,content_type="application/json")
    response_body={ 'status code': 404,
               'body': 'INVALID POST/WRONG DATA',
               }
    return HttpResponseNotFound(json.dumps(response_body),content_type="application/json")
