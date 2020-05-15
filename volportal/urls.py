"""volportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from authentication.views import signup
from authentication.views import welcome
from campaign.views import campaign_home
from campaign.views import campaign_delete
from volunteer.views import volunteer_home
from volunteer.views import add_volunteer
from volunteer.views import edit_volunteer
from volunteer.views import delete_volunteer
from volunteer.views import confirmed_volunteer
from task.views import task_home
from task.views import add_task
from task.views import task_add
from task.views import task_edit
from task.views import task_delete
from task.views import verify_email
from settingsapp.views import settings_home
from settingsapp.views import send_mail_setup
from settingsapp.views import change_password
from settingsapp.views import delete_account
from sendmail.views import notify

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome.HomePageView.as_view(), name="welcome"),
    path('home/campaign', campaign_home.HomePageView.as_view(), name="campaign_home"),
    path('home/campaign_delete/<int:campaign_id>', campaign_delete.DeleteCampaignView.as_view(), name="campaign_delete"),
    path('home/volunteer/<int:campaign_id>', volunteer_home.HomePageView.as_view(), name="volunteer_home"),
    path('home/volunteer/add/<int:campaign_id>', add_volunteer.HomePageView.as_view(), name="add_volunteer"),
    path('home/volunteer/edit/<int:campaign_id>/<str:volunteer_id>/<int:id>', edit_volunteer.HomePageView.as_view(), name="edit_volunteer"),
    path('home/delete_volunteer/<int:campaign_id>/<str:volunteer_id>/<int:id>', delete_volunteer.DeleteVolunteerView.as_view(), name="delete_volunteer"),
    path('home/confirmed/<int:campaign_id>/<str:volunteer_id>/<int:id>', confirmed_volunteer.ConfirmedView.as_view(), name="confirmed_volunteer"),
    path('home/task/<int:campaign_id>/<str:volunteer_id>/<int:id>', task_home.HomePageView.as_view(), name="task_home"),
    path('home/task/add/<int:campaign_id>/<str:volunteer_id>/<int:id>', add_task.HomePageView.as_view(), name="add_task"),
    path('home/task_add/<int:campaign_id>/<str:volunteer_id>/<int:id>/<str:task_id>', task_add.HomePageView.as_view(), name="task_add"),
    path('home/task_edit/<int:campaign_id>/<str:volunteer_id>/<int:id>/<str:task_id>', task_edit.HomePageView.as_view(), name="task_edit"),
    path('home/task_delete/<int:campaign_id>/<str:volunteer_id>/<int:id>/<str:task_id>', task_delete.DeleteTaskView.as_view(), name="task_delete"),
    path('home/settings', settings_home.HomePageView.as_view(), name="settings_home"),
    path('home/send_mail_settings', send_mail_setup.HomePageView.as_view(), name="send_mail_setup"),
    path('home/change_password_settings', change_password.ChangePasswordPage.as_view(), name="change_password"),    
    path('home/delete_account', delete_account.DeleteAccount.as_view(), name="delete_account"),
    path('home/verify_email/<int:campaign_id>/<str:volunteer_id>/<int:id>', verify_email.VerifyEmailView.as_view(), name="verify_email"),
    path('home/task/notify_volunteer', notify.SendMailPage.as_view(), name='notify_volunteer'),
    path('signup', signup.SignUpView.as_view(), name='signup'),
    path('login', LoginView.as_view(template_name="login_form.html"), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
]
