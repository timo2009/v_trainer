from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "v_trainer/index.html"

class listView(TemplateView):
    template_name = "v_trainer/neuer_test.html"

class anleitung(TemplateView):
    template_name = "v_trainer/anleitung.html"

class vokabeltestliste(TemplateView):
    template_name = "v_trainer/vokabeltestliste.html"

class RadioReady(TemplateView):
    template_name = "v_trainer/radio_ready.html"

class NutzerDaten(TemplateView):
    template_name = "v_trainer/daten_nutzer.html"



