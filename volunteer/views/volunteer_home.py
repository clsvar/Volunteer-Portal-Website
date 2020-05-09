from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from campaign.models import Campaign
from volunteer.models import Volunteer_Details
from task.models import Task_Details

class HomePageView(View):

    def get(self, request, campaign_id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        campaign = Campaign.objects.get(pk=campaign_id)

        volunteers = Volunteer_Details.objects.filter(campaign_id=campaign_id)

        #look for tasks according to volunteer_id
        #tasks_exist = Task_Details.objects.filter(user_id=request.user.id, campaign_id=campaign_id)

        template_name = "volunteer_home.html"

        data = {'user': request.user, 'campaign': campaign, 'volunteers': volunteers}

        return render(request, template_name, data)
