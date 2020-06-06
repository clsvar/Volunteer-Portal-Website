from django.views.generic import View
from django.shortcuts import render, redirect

from volunteer.models import Volunteer_Details
from task.models import Task_Details

class DeleteTaskView(View):

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

        task = Task_Details.objects.filter(id=task_id)
        if task:
            task.delete()

        return redirect('task_home' , campaign_id, volunteer_id, id)
