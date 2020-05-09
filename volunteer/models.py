from django.db import models

from django.contrib.auth.models import User
from campaign.models import *

from django.utils import timezone
# Volunteer Portal Database version 1.2
# Create your models here.
VOLUNTEER_STATUS_CHOICES = (
    ('A', 'Available'),
    ('B', 'Busy'),
    ('I', 'Inactive')
)
class Volunteer_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    volunteer = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    status = models.CharField(max_length=20, choices=VOLUNTEER_STATUS_CHOICES)
    campaign = models.ForeignKey("campaign.Campaign", on_delete=models.CASCADE,) #name_id = campaign_id
    date_created = models.DateTimeField("date created", auto_now=True)

    def __str__(self):
        return self.volunteer #changes volunter object to number
