from django.forms import ModelForm
from django import forms
from django.core import validators

from task.models import Task_Details

import datetime

class TaskEditDetailsForm(ModelForm):
    class Meta:
        model = Task_Details
        exclude = ['user', 'campaign', 'volunteer', 'date_created']
