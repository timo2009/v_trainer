from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from v_trainer.models import EnglischTestEineVokalel, DeutschesWort
from django.urls import reverse_lazy
from django.utils import timezone


class EnglischTestEineVokalelCreate(CreateView):
    model = EnglischTestEineVokalel
    fields = ['user', 'englisches_wort_1']
    success_url = reverse_lazy('englischtest_1_vokabel_list')

    # template_name = 'englischtesteinevokalel_form.html'


class EnglischTestEineVokalelUpdate(UpdateView):
    model = EnglischTestEineVokalel
    fields = ['user', 'englisches_wort_1', 'antwort_englisches_wort_1']
    success_url = reverse_lazy('englischtest_1_vokabel_list')
    # template_name = 'englisch_test_update_form'


class EnglischTestEineVokalelList(ListView):
    model = EnglischTestEineVokalel


class EnglischTestEineVokalelDetail(DetailView):
    model = EnglischTestEineVokalel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_dwort_list'] = DeutschesWort.objects.all()
        context['test'] = DeutschesWort.objects.filter(wort=EnglischTestEineVokalel.antwort_englisches_wort_1)
        # context['all_dwort_list'] = DeutschesWort.filter(products__product_company=company)
        return context

