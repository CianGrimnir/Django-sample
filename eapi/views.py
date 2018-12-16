from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse

def index(request):
    response_data1 = {'foo':'bar'}
    response_data = request.method
    return HttpResponse(response_data)
    #return HttpResponse(json.dumps(response_data), content_type="application/json")
