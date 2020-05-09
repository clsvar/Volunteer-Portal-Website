from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError

from volunteer.models import *

from volunteer.forms.volunteer_edit_form import *



class HomePageView(View):

    def get(self, request, campaign_id, volunteer_id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        campaign = Campaign.objects.get(pk=campaign_id)

        volunteer = Volunteer_Details.objects.get(campaign=campaign_id, volunteer=volunteer_id)

        voleditdetform = VolunteerEditDetailsForm(instance=volunteer)

        template_name = "edit_volunteer.html"

        data = {'user': request.user, 'campaign': campaign, 'volunteer': volunteer, 'voleditdetform': voleditdetform}

        return render(request, template_name, data)

    def post(self, request, campaign_id, volunteer_id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        # try:
        volunteer = Volunteer_Details.objects.get(campaign=campaign_id, volunteer=volunteer_id)
        form = VolunteerEditDetailsForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()

            return redirect("volunteer_home", campaign_id)
        else:
            campaign = Campaign.objects.get(pk=campaign_id)

            #volunteer = Volunteer_Details.objects.get(campaign=campaign_id, volunteer=volunteer_id)

            voleditdetform = form

            template_name = "edit_volunteer.html"

            data = {'user': request.user, 'campaign': campaign, 'volunteer': volunteer, 'voleditdetform': voleditdetform}

            return render(request, template_name, data)

        # except IntegrityError as e:
        #     messages.info(request, 'Volunteer email must be unique!') #this unique email check is not needed anymore.
        #     return redirect("edit_volunteer", campaign_id, volunteer_id)
