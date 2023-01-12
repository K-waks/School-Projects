from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "home/register.html"
    success_url = "/accounts/login/"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"
