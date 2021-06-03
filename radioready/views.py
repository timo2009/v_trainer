from django.utils import timezone
from django.views.generic.list import ListView

from radioready.models import RadioShow


class RadioShowListView(ListView):
    model = RadioShow
