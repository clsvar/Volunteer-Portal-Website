from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from volunteer.models import *

from task.forms.sendmail_form import *
from settingsapp.models import Settings_Details

from task.views.services import VolunteerPortalServices

class VerifyEmailView(View):

    def get(self, request, campaign_id, volunteer_id, id):
        if request.user.is_authenticated:
            volunteer = Volunteer_Details.objects.get(campaign_id=campaign_id, volunteer=volunteer_id, id=id)
            if request.user.id == volunteer.user_id:
                pass
            else:
                return redirect('login')
        else:
            return redirect('login')

        campaign = Campaign.objects.get(pk=campaign_id)

        volunteer = Volunteer_Details.objects.get(campaign_id=campaign_id, volunteer=volunteer_id, id=id)
        #form to check email and password that is saved in settings page.
        form = SendMailForm()

        template_name = "verify_email.html"

        data = {'user': request.user, 'campaign': campaign, 'volunteer': volunteer, 'form': form }

        return render(request, template_name, data)

    def post(self, request, campaign_id, volunteer_id, id):
        if request.user.is_authenticated:
            volunteer = Volunteer_Details.objects.get(campaign_id=campaign_id, volunteer=volunteer_id, id=id)
            if request.user.id == volunteer.user_id:
                pass
            else:
                return redirect('login')
        else:
            return redirect('login')

        form = SendMailForm(request.POST)

        if form.is_valid():
            password_verified = Settings_Details.objects.filter(email=request.POST['email'] ,password=VolunteerPortalServices.hash_pass(request.POST['password']))
            #if email and password is correct, create session cookies.
            if password_verified:
                request.session['verified'] = request.POST['password']
                request.session['email'] = request.POST['email']
            else:
                request.session['verified'] = False

        return redirect("task_home", campaign_id, volunteer_id, id)
