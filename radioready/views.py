from lib2to3.fixes.fix_input import context
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from radioready.models import RadioShow, SongWishes, Kommentare
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime


class RadioShowListView(LoginRequiredMixin, ListView):
    model = RadioShow


class RadioShowDetail(DetailView):
    model = RadioShow


class RadioAndenken(TemplateView):
    template_name = "radioready/radioandenken.html"


class NutzerDaten(TemplateView):
    template_name = "radioready/daten_und_nutzer.html"


class RadioNewsletter(TemplateView):
    template_name = "radioready/newsletter.html"


class StyleCss(TemplateView):
    template_name = "radioready/style.css"


class SongWishesCreate(CreateView):
    model = SongWishes
    fields = ["song", "author"]
    success_url = reverse_lazy('songwishes_list')
    template_name = 'radioready/songwish_create.html'

    # https://stackoverflow.com/questions/5785727/accessing-request-user-in-class-based-generic-view-createview-in-order-to-set-fk
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        return super(SongWishesCreate, self).form_valid(form)


class SongWishesList(ListView):
    model = SongWishes
    template_name = "radioready/songwishes_list.html"

class KommentareUpdate(UpdateView):
    model = Kommentare
    fields = ['kommentar', 'kommentar_antwort']
    success_url = reverse_lazy('kommentare_list')

class KommentareCreate(CreateView):
    model = Kommentare
    fields = ['kommentar']
    success_url = reverse_lazy('kommentare_list')
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        return super(KommentareCreate, self).form_valid(form)

class KommentareList(ListView):
    model = Kommentare