from django.db import models
from django.utils import timezone

# Create your models here.
class restreg(models.Model):
  restname=models.CharField(max_length=100)
  restpass=models.CharField(max_length=20, null=True,blank=True)
  restemail=models.EmailField()
  restphone=models.BigIntegerField()
  restlicense=models.FileField(upload_to="restlicense") #upload file
  restimg=models.FileField(upload_to="restimg",null=True,blank=True) #upload file
  restplace=models.CharField(max_length=20,null=True,blank=True)
  restdist=models.CharField(max_length=20,null=True,blank=True)
  reststate=models.CharField(max_length=20,null=True,blank=True)
  restpin=models.IntegerField(null=True,blank=True)
  opentime=models.CharField(max_length=20,null=True,blank=True)
  closetime=models.CharField(max_length=20,null=True,blank=True)
  approve=models.BooleanField(default=False)
  restrating=models.IntegerField(null=True,blank=True)
  joindate= models.DateTimeField(default=timezone.now)
  status=models.BooleanField(default=False)

  def __str__(self):
    return self.restname

class Category(models.Model):
  catname=models.CharField(max_length=20)
  restid=models.ForeignKey(restreg,on_delete=models.CASCADE,null=True,blank=True)
  status=models.BooleanField(default=False)

  def __str__(self):
    return self.catname

class Menu(models.Model):
  iname=models.CharField(max_length=20)
  img=models.FileField(upload_to="itemimg") #upload file
  catid=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
  restid=models.ForeignKey(restreg,on_delete=models.CASCADE,null=True,blank=True)
  iprice=models.IntegerField()
  idesc=models.CharField(max_length=200)
  offer=models.IntegerField()
  preptime=models.CharField(max_length=20)
  itype=models.CharField(max_length=20)
  irate=models.IntegerField(null=True,blank=True)
  status=models.BooleanField(default=False)
  cart_status=models.BooleanField(default=False)



  
  def __str__(self):
     return self.iname