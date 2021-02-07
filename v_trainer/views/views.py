from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "v_trainer/index.html"
