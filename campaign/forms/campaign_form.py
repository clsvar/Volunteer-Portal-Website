from django.forms import ModelForm

from campaign.models import Campaign


class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        exclude = ['user','date_created']
