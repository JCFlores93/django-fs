from django.shortcuts import render
from django.http import HttpResponse
#Utilities
from datetime import datetime

# Create your views here.
def hello_world(req):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current server time is {now}'.format(now=str(now)))
