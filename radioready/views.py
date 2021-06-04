from django.utils import timezone
from django.views.generic.list import ListView

from radioready.models import RadioShow, RadioUser


class RadioShowListView(ListView):
    model = RadioShow

class RadioUserListView(ListView):
    model = RadioUser
