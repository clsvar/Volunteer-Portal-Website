from django.db import models

from django.contrib.auth.models import User
from campaign.models import *
from volunteer.models import *

from django.utils import timezone
# Volunteer Portal Database version 1.2
# Create your models here.

class Task_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    campaign = models.ForeignKey("campaign.Campaign", on_delete=models.CASCADE,)
    volunteer = models.ForeignKey("volunteer.Volunteer_Details", on_delete=models.CASCADE,)
    task_name = models.CharField("Task_Name", max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    #*address*
    number = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    #*contact person*
    family_name = models.CharField(max_length=50)
    #*sent_mail*
    notified = models.BooleanField(default=False)    
    date_created = models.DateTimeField("date created", auto_now=True)
