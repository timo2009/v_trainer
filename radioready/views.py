from lib2to3.fixes.fix_input import context

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from radioready.models import RadioShow, SongWishes
from django.contrib.auth.mixins import LoginRequiredMixin




class RadioShowListView(LoginRequiredMixin, ListView):
    model = RadioShow





class RadioAndenken(TemplateView):
    template_name = "radioready/radioandenken.html"

class NutzerDaten(TemplateView):
    template_name = "radioready/daten_und_nutzer.html"

class RadioNewsletter(TemplateView):
    template_name = "radioready/newsletter.html"




class SongWishesCreate(CreateView):
    model = SongWishes
    fields = ['user', 'song_wishes', "author"]
    success_url = reverse_lazy('songwishes_list')
    # template_name = 'song_wishes_update_form'



