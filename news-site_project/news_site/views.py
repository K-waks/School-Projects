from datetime import datetime
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"
    extra_context = {"today": datetime.today()}
