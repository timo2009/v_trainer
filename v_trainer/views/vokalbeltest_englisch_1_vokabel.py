from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from v_trainer.models import EnglischTestEineVokalel, DeutschesWort, EnglischesWort
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
        # Hiermit hole ich mir das zu dem Englischtest gehörende englische Wort
        englisches_wort = self.object.englisches_wort_1
        print('englisches_wort.dwort')
        print(englisches_wort.dwort)
        print('type(englisches_wort.dwort)')
        print(type(englisches_wort.dwort))

        context['englisches_wort'] = englisches_wort
        context['deutsche_woerter'] = englisches_wort.dwort.all()

        ergebnis = 'falsch'

        for wort in englisches_wort.dwort.all():

            if wort.wort == self.object.antwort_englisches_wort_1:
                ergebnis = 'richtig'

        context['ergebnis'] = ergebnis
        if ergebnis == "richtig":
            context['preis'] = 1

        if ergebnis == "falsch":
            context['preis'] = 2

        liste = [2]

        if liste:
            print("True")
        else:
            print("False")
        return context
