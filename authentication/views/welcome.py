from django.views.generic import View
from django.shortcuts import render, redirect

class HomePageView(View):

    def get(self, request):

        template_name = "welcome.html"

        data = {}

        return render(request, template_name, data)
