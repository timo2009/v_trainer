from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "v_trainer/index.html"

class listView(TemplateView):
    template_name = "v_trainer/neuer_test.html"

class anleitung(TemplateView):
    template_name = "v_trainer/anleitung.html"

class vokabeltestliste(TemplateView):
    template_name = "v_trainer/vokabeltestliste.html"


