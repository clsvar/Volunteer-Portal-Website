from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm



class ChangePasswordPage(View):

    def get(self, request):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        form = PasswordChangeForm(request.user)

        template_name = "change_password.html"

        data = {'user': request.user, 'form': form}

        return render(request, template_name, data)

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()

            return redirect("settings_home")
        else:
            messages.error(request, 'Please correct the error above!')

            template_name = "change_password.html"

            data = {'user': request.user, 'form': form}

            return render(request, template_name, data)
