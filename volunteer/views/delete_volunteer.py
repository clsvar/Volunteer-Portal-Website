from django.views.generic import View
from django.shortcuts import render, redirect

from campaign.models import Campaign
from volunteer.models import Volunteer_Details

class DeleteVolunteerView(View):

    def get(self, request, campaign_id, volunteer_id, id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        campaign = Campaign.objects.get(pk=campaign_id)

        volunteer = Volunteer_Details.objects.get(campaign=campaign_id, volunteer=volunteer_id, id=id)
        if volunteer:
            volunteer.delete()

        return redirect('volunteer_home' , campaign_id)
