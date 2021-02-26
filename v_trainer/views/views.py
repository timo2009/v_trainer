from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "v_trainer/index.html"

class anleitung(TemplateView):
    template_name = "v_trainer/anleitung.html"


