from django.forms import ModelForm

from settingsapp.models import Settings_Details


class SendMailForm(ModelForm):
    class Meta:
        model = Settings_Details
        exclude = ['user','date_created']
