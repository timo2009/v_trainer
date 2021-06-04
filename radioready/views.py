from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from radioready.models import RadioShow, RadioUser


class RadioShowListView(ListView):
    model = RadioShow

class RadioUserListView(ListView):
    model = RadioUser

class RadioAndenken(TemplateView):
    template_name = "radioready/radioandenken.html"

