from django.db import models
from django.utils import timezone
from restapp.models import*
# Create your models here.
class userreg(models.Model):
    uname=models.CharField(max_length=20)
    upass=models.CharField(max_length=20)
    uemail=models.EmailField()
    uphone=models.BigIntegerField()
    dob=models.DateField()
    upalce=models.CharField(max_length=20,null=True,blank=True)
    udist=models.CharField(max_length=20,null=True,blank=True)
    upin=models.IntegerField(null=True,blank=True)
    joindate= models.DateTimeField(default=timezone.now)
    status=models.BooleanField(default=False)

    
    def __str__(self):
     return self.uname

class Cart(models.Model):
    userid=models.ForeignKey(userreg, on_delete=models.CASCADE,null=True,blank=True)
    menuid=models.ForeignKey(Menu, on_delete=models.CASCADE,null=True,blank=True)
    restid=models.ForeignKey(restreg, on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(default=timezone.now)
    payment_status=models.BooleanField(default=False)
    

class Order(models.Model):
    userid=models.ForeignKey(userreg, on_delete=models.CASCADE,null=True,blank=True)
    cartid=models.ManyToManyField(Cart,null=True,blank=True)
    orderid=models.IntegerField(null=True,blank=True)
    status=models.BooleanField(default=True)

   

