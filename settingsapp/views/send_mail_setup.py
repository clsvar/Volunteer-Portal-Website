from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from settingsapp.forms.sendmail_form import *

from settingsapp.views.services import VolunteerPortalServices
from campaign.models import Campaign
from settingsapp.models import Settings_Details

class HomePageView(View):

    def get(self, request):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')
        #get email address of user.
        email_address = Settings_Details.objects.filter(user__username=str(request.user))

        template_name = "send_mail_setup.html"

        form = SendMailForm()

        data = {'user': request.user, 'form': form, 'email_address': email_address}

        return render(request, template_name, data)

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        form = SendMailForm(request.POST)

        if form.is_valid():
            emailsettings = Settings_Details.objects.filter(user__username=request.user)
            if emailsettings:
                #if email details already exists for user.
                emailsettings[0].email = request.POST['email']
                emailsettings[0].password = VolunteerPortalServices.hash_pass(request.POST['password'])
                emailsettings[0].save()
                try:
                    del request.session['verified']
                    del request.session['email']
                except KeyError:
                    pass
            else:
                #if new email setting details.
                sendmail = form.save(commit=False)
                sendmail.user = request.user
                sendmail.password = VolunteerPortalServices.hash_pass(request.POST['password'])
                sendmail.save()

            return redirect("settings_home")
        else:
            template_name = "settings_home"
            data = {}
            return render(request, template_name, data)
