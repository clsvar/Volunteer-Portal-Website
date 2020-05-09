from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from settingsapp.forms.delete_account_form import *



class DeleteAccount(View):
    def purge_all(request):
        user_account = User.objects.get(username=str(request.user))
        user_account.delete()

    def get(self, request):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        user_account = User.objects.get(username=str(request.user))

        template_name = "delete_account.html"

        data = {'user': request.user, 'user_account': user_account}

        return render(request, template_name, data)

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            pass
        else:
            return redirect('login')

        DeleteAccount.purge_all(request)
        #delete cookies
        request.session.clear()
        return HttpResponse("<script>alert('Your Account has been deleted. Logging out...');window.location = '/'</script>")
