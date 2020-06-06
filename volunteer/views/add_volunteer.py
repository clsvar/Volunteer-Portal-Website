from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from volunteer.models import *

from volunteer.forms.volunteer_form import *



class HomePageView(View):

    def get(self, request, campaign_id):
        if request.user.is_authenticated:
            campaign = Campaign.objects.get(pk=campaign_id)
            if request.user.id == campaign.user_id:
                pass
            else:
                return redirect('login')
        else:
            return redirect('login')

        campaign = Campaign.objects.get(pk=campaign_id)

        voldetform = VolunteerDetailsForm()

        template_name = "add_volunteer.html"

        data = {'user': request.user, 'campaign': campaign, 'voldetform': voldetform}

        return render(request, template_name, data)

    def post(self, request, campaign_id):
        if request.user.is_authenticated:
            campaign = Campaign.objects.get(pk=campaign_id)
            if request.user.id == campaign.user_id:
                pass
            else:
                return redirect('login')
        else:
            return redirect('login')

        form = VolunteerDetailsForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.user = request.user
            volunteer.campaign_id = campaign_id
            volunteer.save()

            return redirect("volunteer_home", campaign_id)
        else:
            campaign = Campaign.objects.get(pk=campaign_id)

            voldetform = form

            template_name = "add_volunteer.html"

            data = {'user': request.user, 'campaign': campaign, 'voldetform': voldetform}

            return render(request, template_name, data)
