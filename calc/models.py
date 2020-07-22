from django.db import models

# Create your models here.
class Calculator(models.Model):
    value1=models.IntegerField(default=0)
    value2=models.IntegerField(default=0)
    operation=models.CharField(default=0,max_length=1)
    output=models.IntegerField(default=0)