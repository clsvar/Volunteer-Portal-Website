from django.views.generic import View
from django.shortcuts import render, redirect

from task.models import Task_Details

class DeleteTaskView(View):

    def get(self, request, campaign_id, volunteer_id, id, task_id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        task = Task_Details.objects.filter(id=task_id)
        if task:
            task.delete()

        return redirect('task_home' , campaign_id, volunteer_id, id)
