from django.db import models

from django.contrib.auth.models import User

# Volunteer Portal Database version 1.2
# Create your models here.
class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.CharField("Campaign Name", max_length=50, unique=True)
    date_created = models.DateTimeField("date created", auto_now=True)
