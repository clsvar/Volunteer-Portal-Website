from django.views.generic import View
from django.shortcuts import render, redirect

from campaign.models import Campaign

class DeleteCampaignView(View):

    def get(self, request, campaign_id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        campaign = Campaign.objects.filter(pk=campaign_id)
        if campaign:
            campaign.delete()

        return redirect('campaign_home')
