from django.shortcuts import render
from django.http import HttpResponse
#Utilities
from datetime import datetime
import json

# Create your views here.
def hello_world(req):
    return HttpResponse('Current server time is {now}'.format(now=str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs'))))

def returnOK(req):
    print(req)
    numbers = [int(i) for i in req.GET['numbers']]
    sorted_ints = sorted(numbers)
    data= {
        'status': 'ok',
        'number': sorted_ints,
        'message': 'Integers sorted successfully.'

    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def retur_say_hi(req,name,age):
    print(req)
    if age < 12:
        message = 'Sorry {}, you are not allowd here'.format(name)
    else :
        message = 'Helloi {}, you are allowd here'.format(name)
    response= {
        'message': message

    }
    return HttpResponse(json.dumps(response), content_type='application/json')