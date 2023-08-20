from django.shortcuts import render
from django.http import HttpResponse
from .models import DCAParameter

def index(request):
    dca_parameter = DCAParameter.objects.all()
    for param in dca_parameter:
        print(param.exchange_id)
        print(param.exchange_description)
    return HttpResponse('Mi Propio DCA')
