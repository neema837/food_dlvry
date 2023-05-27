from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from restapp.models import*
from django.contrib import messages
# Create your views here.

def index(request):
  restall=restreg.objects.all()
  context={
      'restall':restall
   }
  return render(request,'index.html',context)



def demoindex(request):
  restall=restreg.objects.all()
  context={
      'restall':restall
   }
  return render(request,'demoindex.html',context)