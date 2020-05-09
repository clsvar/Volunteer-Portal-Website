from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from campaign.forms.campaign_form import *

from campaign.models import Campaign

class HomePageView(View):

    def get(self, request):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        form = CampaignForm()

        campaign_user = request.user
        #get all campaigns
        campaign_list = Campaign.objects.filter(user=campaign_user.id)

        if campaign_list:
            pass

        template_name = "campaign_home.html"

        data = {'user': request.user, 'form': form , 'campaign_list': campaign_list}

        return render(request, template_name, data)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.user = request.user
            campaign.save()
            return redirect("campaign_home")
        else:
            template_name = "campaign_home"
            data = {'form': form}
            return render(request, template_name, data)
