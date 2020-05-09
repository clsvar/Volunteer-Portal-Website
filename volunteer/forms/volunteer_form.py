from django.forms import ModelForm

from volunteer.models import Volunteer_Details


class VolunteerDetailsForm(ModelForm):
    class Meta:
        model = Volunteer_Details
        exclude = ['user', 'campaign', 'date_created']
