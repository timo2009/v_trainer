from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from v_trainer.models.deutschtest_1_vokabel import DeutschTestEineVokalel
from v_trainer.models import EnglischTestEineVokalel, DeutschesWort, EnglischesWort
from django.urls import reverse_lazy
from django.utils import timezone


class DeutschTestEineVokalelCreate(CreateView):
    model = DeutschTestEineVokalel
    fields = ['user', 'deutsches_wort_1']
    success_url = reverse_lazy('deutschtest_1_vokabel_list')

    # template_name = 'englischtesteinevokalel_form.html'


class DeutschTestEineVokalelUpdate(UpdateView):
    model = DeutschTestEineVokalel
    fields = ['user', 'deutsches_wort_1', 'antwort_deutsches_wort_1']
    success_url = reverse_lazy('deutschtest_1_vokabel_list')
    # template_name = 'englisch_test_update_form'


class DeutschTestEineVokalelList(ListView):
    model = DeutschTestEineVokalel


class DeutschTestEineVokalelDetail(DetailView):
    model = DeutschTestEineVokalel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Hiermit hole ich mir das zu dem Englischtest gehörende englische Wort
        deutsches_wort = self.object.deutsches_wort_1
        print('deutsches_wort.ewort')
        print(deutsches_wort.ewort)
        print('type(deutsches_wort.ewort)')
        print(type(deutsches_wort.ewort))

        context['deutsches_wort'] = deutsches_wort
        context['englische_woerter'] = deutsches_wort.dwort.all()

        ergebnis = 'falsch'

        for wort in deutsches_wort.dwort.all():

            if wort.wort == self.object.antwort_deutsches_wort_1:
                ergebnis = 'richtig'

        context['ergebnis'] = ergebnis

        return context
