from datetime import date
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import*
from restapp.models import*
from django.contrib import messages
from django.urls import reverse
# Create your views here.

#def index(request):
    #return render(request,'index.html')
def login(request):
 if request.method=='POST':
        try:
            uemail=request.POST['uemail']
            upass=request.POST['upass']
           
            check=userreg.objects.get(uemail=uemail,upass=upass)
            request.session['id']=check.id
            request.session['uname']=check.uname
            return redirect('userhome')
        except userreg.DoesNotExist as e:
            messages.info(request,'Invalid User')
 return render(request,'user/login.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        uphone=request.POST['uphone']
        upass=request.POST['upass']
        repass=request.POST['repass']
        dob=request.POST['dob']
        if upass==repass:
           if userreg.objects.filter(uemail=uemail).exists():
            value="name"
            messages.info(request,'user already exists')
            return render(request,'user/signup.html',{'n':value})

           else:
             saveval=userreg(uname=uname,uemail=uemail,uphone=uphone,upass=upass,dob=dob)
             print("user created")
             saveval.save()
             return redirect('login')
        else:
          p="pass"
          messages.info(request,'Password not same !!') 
          return render(request,'user/signup.html',{'p':p})
    return render(request,'user/signup.html')

def verification(request):
    return render(request,'user/verification.html')

def userhome(request):
    restall=restreg.objects.all()
    context={
        'restall':restall
     }
    return render(request,'user/userhome.html',context)

def restdetails(request,rid):

    if 'id' not in request.session :
       messages.error(request, 'Please login first.')
       return redirect('login')
    
    else:
        
        restall = restreg.objects.get(id=rid)
        global crt_item 
        crt_item = None
        categories = Category.objects.filter(restid=rid)
        uid = request.session['id']
        cartitem=Cart.objects.filter(userid_id=uid) 
       
        if request.method == 'POST':
                userid = request.session['id']
                menuid = request.POST['menuid']
                add_times_cart = Cart(userid_id=userid,menuid_id=menuid,restid_id=rid)
                add_times_cart.save()
                Menu.objects.filter(id=menuid).update(cart_status=True)
                messages.success(request, 'Item added to cart successfully.')
        
         
        price=itotal=total=0
        
        
        for i in cartitem:
          price = i.menuid.iprice * i.quantity
          itotal = itotal + price 
          
        total=itotal
     
        if total>250 and total<500:
             delcharge=20
        elif total<250:
             delcharge=10
        elif total>=500 and total<1000:
             delcharge=40
        elif total>=1000 and total<2000:
             delcharge=60
        elif total>=2000:
             delcharge=90
        context ={
                     'restall':restall ,
                     'categories':categories,
                     'cartitem':cartitem,
                     'total':total,
                     'delcharge':delcharge,
                       
                }
        
        

        return render(request,'user/restdetails.html',context)


                 # Check if the cart already contains items from another restaurant
                  
                # if menu.restid == rid:
                        # if Cart.objects.filter(menuid=menu.id).exists():
                        #         cart = Cart.objects.filter(menuid=menu.id)
                        #         for c in cart:
                        #             print(c.id)
                        #             cart_id = c.id
                        #         print(cart_id)
                        #         cart = get_object_or_404(Cart, pk=cart_id)
                        #         cart.quantity += 1
                        #         cart.save()
                        # else:

                    #         saveval = Cart(userid_id=userid,restid_id=restid.id, menuid_id=menu.id, quantity=quantity)  # Pass the menu id
                    #         saveval.save()

                    #     messages.success(request, 'Item added to cart successfully.')
                    # else:
                    #     messages.error(request, 'Please remove items from another restaurant before adding new items.')

                        
       
    



def increment_quantity(request,cart_id):
                cart = get_object_or_404(Cart, pk=cart_id)
                cart.quantity += 1
                cart.save()
                print(cart.restid.id)
                return redirect('restdetails',rid=cart.restid.id) 

 

def decrement_quantity(request,cart_id):

            cart = get_object_or_404(Cart, pk=cart_id)
            if cart.quantity == 1:
                        cart.delete()
            else:
                cart.quantity -= 1
                cart.save()        
            return redirect('restdetails', rid=cart.restid.id) 


def checkout(request):
        crt = Cart.objects.filter(userid=request.session['id'])
        price=itotal=total=0

        for i in crt:
          price = i.menuid.iprice * i.quantity
          itotal = itotal + price 
          
        total=itotal
     
        if total>250 and total<500:
             delcharge=20
        elif total<250:
             delcharge=10
        elif total>=500 and total<1000:
             delcharge=40
        elif total>=1000 and total<2000:
             delcharge=60
        elif total>=2000:
             delcharge=90
        context = {
             "total" : total,
             "delcharge" : delcharge, 
        }
        return render(request, 'user/checkout.html',context)

# def apply_cart(request):
#     if request.method == 'POST':
#         menu_id = request.POST.get('menu_id')
#         quantity = request.POST.get('quantity')
#         # Process the data as needed
        
#         # Redirect or render a response
        
    
#     return render(request, 'user/restdetails.html')
