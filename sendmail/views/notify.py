from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from volunteer.models import Volunteer_Details
from task.models import Task_Details
from sendmail.views.send_mail import sendMail

class SendMailPage(View):

    def get(self, request):
        #verify user having correct task id.
        task_id = request.GET.get('task_id', None)
        volunteer = Volunteer_Details.objects.get(task_details__id=int(task_id))

        if volunteer.user_id == request.user.id:
            pass
        else:
            return HttpResponse('Error')

        sent_successfully = sendMail(request)
        if sent_successfully:
            task_id = request.GET.get('task_id', None)
            if (task_id):
                task = Task_Details.objects.get(id=int(task_id))
                if task:
                    task.notified = True
                    task.save()
                    return HttpResponse('Sent')
        else:
            return HttpResponse('Error')
