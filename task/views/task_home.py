from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from campaign.models import Campaign
from volunteer.models import Volunteer_Details
from task.models import Task_Details
from settingsapp.models import Settings_Details

from task.views.services import VolunteerPortalServices

class HomePageView(View):

    def get(self, request, campaign_id, volunteer_id, id):
        #check if user is authenticated.
        if request.user.is_authenticated:
            volunteer = Volunteer_Details.objects.get(campaign=campaign_id, volunteer=volunteer_id, id=id)
            if request.user.id == volunteer.user_id:
                pass
            else:
                return redirect('login')
        else:
            return redirect('login')
        #get campaign name
        campaign = Campaign.objects.get(pk=campaign_id)
        #get volunteer details like volunteer id.
        volunteer = Volunteer_Details.objects.get(campaign_id=campaign_id, volunteer=volunteer_id, id=id)
        #get tasks details like name, date, time, address 1, address 2, city, country, family name of customer.
        my_tasks = Task_Details.objects.filter(campaign_id=campaign_id, volunteer_id=volunteer.id)
        #get tasks which belongs to a volunteer.
        tasks = Task_Details.objects.filter(campaign_id=campaign_id).exclude(volunteer_id=volunteer.id)
        #getting session cookies to verify email and password.
        try:
            verified_pass = request.session['verified']
            if verified_pass != None:
                email_pass = Settings_Details.objects.filter(password=VolunteerPortalServices.hash_pass(verified_pass))
                if email_pass:
                    verified = True
                else:
                    verified = False
            else:
                verified = False
        except:
            verified = False

        #get volunteer id using task volunteer id.
        volunteers = Volunteer_Details.objects.all()

        template_name = "task_home.html"

        data = {'user': request.user, 'campaign': campaign, 'volunteer': volunteer , 'tasks': tasks, 'my_tasks': my_tasks, 'verified': verified, 'volunteers': volunteers}

        return render(request, template_name, data)
