
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from django.contrib import messages
# Create your views here.

#def index(request):
    #return render(request,'index.html')
def adlogin(request):
    if request.method=='POST':
        try:
            demail=request.POST['demail']
            dpass=request.POST['dpass']
           
            check=delvreg.objects.get(demail=demail,dpass=dpass)
            request.session['id']=check.id
            request.session['demail']=check.demail
            return redirect('index')
        except delvreg.DoesNotExist as e:
            messages.info(request,'Invalid User')
    return render(request,'delivery/dlogin.html')

def adsignup(request):
    if request.method=='POST':
        dname=request.POST['dname']
        demail=request.POST['demail']
        dphone=request.POST['dphone']
        dlicense=request.FILES.get('dlicense') #file upload
        dob=request.POST['dob']
        if delvreg.objects.filter(dname=dname).exists():
           value="name"
           messages.info(request,'user already exists')
           return render(request,'delivery/dsignup.html',{'n':value})

        else:
           saveval=delvreg(dname=dname,demail=demail,dphone=dphone,dlicense=dlicense,dob=dob)
           print("user created")
           saveval.save()
           return redirect('dlogin')
    return render(request,'delivery/dsignup.html')
