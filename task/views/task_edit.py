from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from task.forms.task_edit_form import *

from campaign.models import Campaign
from volunteer.models import Volunteer_Details
from task.models import Task_Details

from datetime import datetime

class HomePageView(View):

    def get(self, request, campaign_id, volunteer_id, id, task_id):
        if request.user.is_authenticated:
            volunteer = Volunteer_Details.objects.get(campaign=campaign_id, volunteer=volunteer_id, id=id)
            if request.user.id == volunteer.user_id:
                tasks = Task_Details.objects.get(pk=task_id)
                if request.user.id == tasks.user_id:
                    pass
                else:
                    return redirect('login')
            else:
                return redirect('login')
        else:
            return redirect('login')

        campaign = Campaign.objects.get(pk=campaign_id)

        volunteer = Volunteer_Details.objects.get(campaign_id=campaign_id, volunteer=volunteer_id, id=id)

        tasks = Task_Details.objects.get(pk=task_id)

        taskeditdetform = TaskEditDetailsForm(instance=tasks)

        template_name = "task_edit.html"

        data = {'user': request.user, 'campaign': campaign, 'volunteer': volunteer , 'tasks': tasks, 'taskeditdetform': taskeditdetform}

        return render(request, template_name, data)

    def post(self, request, campaign_id, volunteer_id, id, task_id):
        if request.user.is_authenticated:
            volunteer = Volunteer_Details.objects.get(campaign=campaign_id, volunteer=volunteer_id, id=id)
            if request.user.id == volunteer.user_id:
                tasks = Task_Details.objects.get(pk=task_id)
                if request.user.id == tasks.user_id:
                    pass
                else:
                    return redirect('login')
            else:
                return redirect('login')
        else:
            return redirect('login')

        volunteer = Volunteer_Details.objects.get(volunteer=volunteer_id, id=id)
        task = Task_Details.objects.get(id=task_id)
        form = TaskEditDetailsForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.campaign_id = campaign_id
            volunteer = Volunteer_Details.objects.get(volunteer=volunteer_id, id=id)
            task.volunteer_id = volunteer.id
            task.save()

            return redirect("task_home", campaign_id, volunteer, id)
        else:
            campaign = Campaign.objects.get(pk=campaign_id)

            volunteer = Volunteer_Details.objects.get(campaign_id=campaign_id, volunteer=volunteer_id, id=id)

            tasks = Task_Details.objects.get(pk=task_id)

            taskeditdetform = form

            template_name = "task_edit.html"

            data = {'user': request.user, 'campaign': campaign, 'volunteer': volunteer , 'tasks': tasks, 'taskeditdetform': taskeditdetform}

            return render(request, template_name, data)
