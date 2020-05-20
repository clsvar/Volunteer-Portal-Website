from django.shortcuts import render, redirect
import urllib

from django.core.mail import send_mail

from volunteer.models import Volunteer_Details
from task.models import Task_Details
# Create your views here.
def sendMail(request):
    try:
        verified = request.session['verified']
        email_from = request.session['email']

        task_id = request.GET.get('task_id', None)
        if (task_id):
            task = Task_Details.objects.get(id=int(task_id))
            nl = '\n'
            msg1 = 'Here is the task we need you to confirm:'
            msg2 = 'task_id: '+ str(task.id)
            msg3 = 'task name: '+ str(task.task_name)
            msg4 = 'task date: ' + str(task.date)
            msg5 = 'task time: '+ str(task.time)
            msg6 = 'address number: '+ str(task.number)
            msg7 = 'address 1: '+ str(task.address_1)
            msg8 = 'address 2: '+ str(task.address_2)
            msg9 = 'city: '+ str(task.city)
            msg10 = 'zip code: '+ str(task.zip_code)
            msg11 = 'country: '+ str(task.country)
            msg12 = 'family name: '+ str(task.family_name)
            mapstr = str(task.number) + ' ' + str(task.address_1) + ' ' + str(task.address_2) + ' ' + str(task.city) + ' ' + str(task.country)
            msg13 = 'Google Map: ' + str('https://www.google.com/maps/search/' + urllib.parse.quote_plus(mapstr))
            msg14 = 'We thank you for your unwavering service.'

            message = '{0} {14} {14} {1}, {14} {2}, {14} {3}, {14} {4}, {14} {5}, {14} {6}, {14} {7}, {14} {8}, {14} {9}, {14} {10}, {14} {11}, {14} {12} {14} {14} {13} {14} {14}'.format(msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9, msg10, msg11, msg12, msg13, msg14, nl)

            #get email address of volunteer from task_details using task_id.
            email_to = Volunteer_Details.objects.get(task_details__id=int(task_id))

            send_mail(
                'Greetings Volunteer!',
                message,
                email_from,
                [str(email_to.email)],
                fail_silently=False,
                auth_user=str(email_from),
                auth_password=verified
                )
            sent_successfully = True
            return sent_successfully
    except Exception as e:
        print('Error sending email.')
        sent_successfully = False
        return sent_successfully
    return redirect("welcome")
