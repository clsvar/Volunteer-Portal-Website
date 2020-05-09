from django.db import models

from django.contrib.auth.models import User

# Volunteer Portal Database version 1.2
# Create your models here.
class Settings_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    email = models.EmailField(max_length=254)
    password = models.CharField("Email Password", max_length=50)
    date_created = models.DateTimeField("date created", auto_now=True)
