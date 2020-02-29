from django.shortcuts import render,reverse
from . import models
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def IndexView(request):
    return HttpResponse('etjmfg')
