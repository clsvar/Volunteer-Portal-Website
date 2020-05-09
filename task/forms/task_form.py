from django.forms import ModelForm

from task.models import Task_Details


class TaskDetailsForm(ModelForm):
    class Meta:
        model = Task_Details
        exclude = ['user', 'campaign', 'volunteer', 'notified', 'date_created']
