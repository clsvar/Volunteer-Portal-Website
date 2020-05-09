from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from volunteer.models import *

class ConfirmedView(View):

    def get(self, request, campaign_id, volunteer_id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        campaign = Campaign.objects.get(pk=campaign_id)

        volunteer = Volunteer_Details.objects.get(campaign=campaign_id, volunteer=volunteer_id)

        volunteer.status = 'U'
        volunteer.save()

        return redirect("volunteer_home", campaign_id)
