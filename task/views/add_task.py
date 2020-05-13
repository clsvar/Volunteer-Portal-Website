from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from volunteer.models import *

from task.forms.task_form import *



class HomePageView(View):

    def get(self, request, campaign_id, volunteer_id, id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        campaign = Campaign.objects.get(pk=campaign_id)

        volunteer = Volunteer_Details.objects.get(campaign_id=campaign.id, volunteer=volunteer_id, id=id)

        taskdetform = TaskDetailsForm()

        template_name = "add_task.html"

        data = {'user': request.user, 'campaign': campaign, 'taskdetform': taskdetform, 'volunteer': volunteer}

        return render(request, template_name, data)

    def post(self, request, campaign_id, volunteer_id, id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        form = TaskDetailsForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.campaign_id = campaign_id
            volunteer = Volunteer_Details.objects.get(volunteer=volunteer_id, id=id)
            task.volunteer_id = volunteer.id
            task.save()

            return redirect("task_home", campaign_id, volunteer_id, id)
        else:
            campaign = Campaign.objects.get(pk=campaign_id)

            volunteer = Volunteer_Details.objects.get(campaign_id=campaign.id, volunteer=volunteer_id, id=id)

            taskdetform = form

            template_name = "add_task.html"

            data = {'user': request.user, 'campaign': campaign, 'taskdetform': taskdetform, 'volunteer': volunteer}

            return render(request, template_name, data)
