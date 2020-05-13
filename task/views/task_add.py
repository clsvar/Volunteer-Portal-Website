from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from campaign.models import Campaign
from volunteer.models import Volunteer_Details
from task.models import Task_Details

class HomePageView(View):

    def get(self, request, campaign_id, volunteer_id, id, task_id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        campaign = Campaign.objects.get(pk=campaign_id)

        volunteer = Volunteer_Details.objects.get(campaign_id=campaign_id, volunteer=volunteer_id, id=id)

        tasks = Task_Details.objects.get(pk=task_id)

        volID = Volunteer_Details.objects.get(id=tasks.volunteer_id)

        template_name = "task_add.html"

        data = {'user': request.user, 'campaign': campaign, 'volunteer': volunteer , 'tasks': tasks, 'volID': volID.volunteer}

        return render(request, template_name, data)

    def post(self, request, campaign_id, volunteer_id, id, task_id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        volunteer = Volunteer_Details.objects.get(volunteer=volunteer_id, id=id)
        task = Task_Details.objects.get(id=task_id)
        task.volunteer_id = volunteer.id
        task.save()

        return redirect("task_home", campaign_id, volunteer_id, id)
