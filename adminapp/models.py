from django.db import models

# Create your models here.
class adminreg(models.Model):
  adname=models.CharField(max_length=20)
  adpass=models.CharField(max_length=20)
