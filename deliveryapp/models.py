from django.db import models
from django.utils import timezone
# Create your models here.
class delvreg(models.Model):
  dname=models.CharField(max_length=20)
  dpass=models.CharField(max_length=20,null=True,blank=True)
  demail=models.EmailField()
  dphone=models.BigIntegerField()
  dlicense=models.FileField(upload_to="dlicense") #upload file
  dob=models.DateField()
  approve=models.BooleanField(default=False)
  joindate= models.DateTimeField(default=timezone.now)
  status=models.BooleanField(default=False)