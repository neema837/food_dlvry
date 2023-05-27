from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from django.contrib import messages
# Create your views here.

#def index(request):
    #return render(request,'index.html')



def ressignup(request):
    if request.method=='POST':
        restname=request.POST['restname']
        restemail=request.POST['restemail']
        restphone=request.POST['restphone']
        restimg=request.FILES.get('restimg') #file upload
        restlicense=request.FILES.get('restlicense') #file upload
        #opentime=request.POST['opentime']
        #closetime=request.POST['closetime']
        #restplace=request.POST['restplace']
        #restdist=request.POST['restdist']
        #reststate=request.POST['reststate'] 
        #restpin=request.POST['restpin']
       
        if restreg.objects.filter(restemail=restemail).exists():
            value="name"
            messages.info(request,'user already exists')
            return render(request,'user/ressignup.html',{'n':value})

        else:
             saveval=restreg(restname=restname,restemail=restemail,restphone=restphone,restlicense=restlicense,restimg=restimg)
             print("user created")
             saveval.save()
             return redirect('reslogin')
        
    return render(request,'restaurant/ressignup.html')


def reslogin(request):
 if request.method=='POST':
        try:
            restemail=request.POST['restemail']
            restpass=request.POST['restpass']
           
            check=restreg.objects.get(restemail=restemail,restpass=restpass)
            request.session['id']=check.id
            request.session['restemail']=check.restemail
            
            if check.restplace is None or check.restdist is None or check.reststate is None or check.restpin is None:
                return redirect('restfill')
            else:

             return redirect('resthome')
        except restreg.DoesNotExist as e:
            messages.info(request,'Invalid User')
 return render(request,'restaurant/reslogin.html')


def resthome(request):
    return render(request,'restaurant/resthome.html')


#--------------------------------------------------------------add category and item-------------------------------------------------------------------------
def addcat(request):
    if request.method=='POST':
        catname=request.POST['catname']
        rid=request.session['id']
        
        saveval=Category(catname=catname,restid_id=rid)
        print("Category inserted successfully!!!")
        saveval.save()
        return redirect('addmenu')
      
    return render(request,'restaurant/addmenu.html')

def addmenu(request):

    if 'id' not in request.session :
       messages.error(request, 'Please login first.')
       return redirect('reslogin')
    else:
     rid = request.session.get('id')
     catall=Category.objects.filter(restid=rid)
     
    
    if request.method=='POST':
        iname=request.POST['iname']
        idesc=request.POST['idesc']
        iprice=request.POST['iprice']
        catid=request.POST['catid']
        restid=request.session['id']
        offer=request.POST['offer']
        img=request.FILES.get('img')
        preptime=request.POST['preptime']
        itype=request.POST['itype']
        menuadd=Menu( iname=iname,idesc=idesc,iprice=iprice,img=img,catid_id=catid,offer=offer,itype=itype,preptime=preptime,restid_id=restid)
        menuadd.save()
        return redirect("newitem")   
    return render(request,'restaurant/addmenu.html',{'catall':catall})

#----------------------------------------------------------------------crud item---------------------------------------------------------------------


def newitem(request):
  
  if 'id' not in request.session :
       messages.error(request, 'Please login first.')
       return redirect('reslogin')
  else:
   rid = request.session.get('id')
   itemid=Menu.objects.filter(restid=rid)
   context={
      'item':itemid
    }
  return render(request,'restaurant/newitem.html',context)


def editmenu(request,pid):
  itemid=Menu.objects.get(id=pid)
  return render(request,'restaurant/editmenu.html',{'itemid':itemid})



def updatemenu(request,uid):
      itemid=Menu.objects.get(id=uid)
      itemid.catall=Category.objects.all()
      if request.method=="POST":
       
        
        itemid.iname=request.POST['iname']
        itemid.idesc=request.POST['idesc']
        itemid. iprice=request.POST['iprice']
        catid=request.POST['catid']
        Menu.objects.filter(id=uid).update(catid_id=catid)
        print(request.POST['catid'])
        itemid.offer=request.POST['offer']
        image_file=request.FILES.get('img')
        if image_file:
            itemid.img = image_file
            itemid.save()
        itemid.preptime=request.POST['preptime']
        itemid.itype=request.POST['itype']
        itemid.save()
        return redirect("newitem")
      return render(request,'restaurant/updatemenu.html',{'itemid':itemid})


def deletemenu(request,did):
    itemid=Menu.objects.get(id=did)
    if request.method=="POST":
      itemid.delete()
      return redirect("newitem")
    return render(request,'restaurant/updatemenu.html',{'itemid':itemid})


#--------------------------------------------------------------------------------------------------------------------------------------------------
def restorder(request):
 
  return render(request,'restaurant/restorder.html')



def restfill(request):
  
  if 'id' not in request.session :
       messages.error(request, 'Please login first.')
       return redirect('reslogin')
  else:
        if request.method == 'POST':
            restplace = request.POST['restplace']
            restdist = request.POST['restdist']
            reststate = request.POST['reststate']
            restpin = request.POST['restpin']
            closetime=request.POST['closetime']
            opentime=request.POST['opentime']
        #Retrieve the Restreg instance associated with the current session ID
            rid = restreg.objects.get(id=request.session['id'])
            
            # Update the Restreg instance with the filled details
            rid.restplace = restplace
            rid.restdist = restdist
            rid.reststate = reststate
            rid.restpin = restpin
            rid.closetime=closetime
            rid.opentime=opentime
            rid.save()  
        
            return redirect('resthome')

  return render(request,'restaurant/restfill.html')

   #opentime=request.POST['opentime']
   #closetime=request.POST['closetime']
   #restplace=request.POST['restplace']
   #restdist=request.POST['restdist']
   #reststate=request.POST['reststate'] 
   #restpin=request.POST['restpin']
     