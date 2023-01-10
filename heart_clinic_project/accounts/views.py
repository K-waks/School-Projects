from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = "/"

    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return redirect("HomeView")
    #     return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = "accounts/login.html"
    extra_context = {
        "message": "Don't have an account? Contact your System Administartor for an account to be created for you."
    }


class LogoutInterfaceView(LogoutView):
    template_name = "accounts/logout.html"
