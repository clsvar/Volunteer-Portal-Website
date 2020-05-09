from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from campaign.models import Campaign

from volunteer.forms.volunteer_form import *

class HomePageView(View):

    def get(self, request, campaign_id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        campaign = Campaign.objects.get(pk=campaign_id)

        voldetform = VolunteerDetailsForm()

        template_name = "create_volunteer.html"

        data = {'user': request.user, 'campaign': campaign, 'voldetform': voldetform}

        return render(request, template_name, data)
