from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from radioready.models import RadioShow
from django.contrib.auth.mixins import LoginRequiredMixin


class RadioShowListView(LoginRequiredMixin, ListView):
    model = RadioShow


class RadioAndenken(TemplateView):
    template_name = "radioready/radioandenken.html"

class NutzerDaten(TemplateView):
    template_name = "radioready/daten_und_nutzer.html"
