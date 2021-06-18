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
    fields = ['user', 'deutsches_wort_1', 'antwort_auf_deutsches_wort_1']
    success_url = reverse_lazy('deutschtest_1_vokabel_list')
    # template_name = 'englisch_test_update_form'


class DeutschTestEineVokalelList(ListView):
    model = DeutschTestEineVokalel


class DeutschTestEineVokalelDetail(DetailView):
    model = DeutschTestEineVokalel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Hiermit hole ich mir das zu dem Deutschtest gehörende englische Wort
        deutsches_wort = self.object.deutsches_wort_1
        antwort_auf_deutsches_wort_1 = self.object.antwort_auf_deutsches_wort_1
        context['deutsches_wort'] = deutsches_wort
        ergebnis = 'falsch'

        moeglische_englischen_antworten = deutsches_wort.list_of_dwords.all()

        print("Mögliche englische Wörter für das deutsch Wort: " + deutsches_wort.wort)
        print("-------------------------------------------------------------")
        for englische_antwort in moeglische_englischen_antworten:
            print("Antwort: " + englische_antwort.wort)

            if antwort_auf_deutsches_wort_1 == englische_antwort.wort:
                print(str(antwort_auf_deutsches_wort_1) + '==' + str(englische_antwort.wort))
                ergebnis = 'richtig'
            else:
                print(str(antwort_auf_deutsches_wort_1 )+ '!=' + str(englische_antwort.wort))

        context['ergebnis_d'] = ergebnis
        if ergebnis == "richtig":
            context['preis'] = 1

        if ergebnis == "falsch":
            context['preis'] = 2

        context['englische_woerter'] = moeglische_englischen_antworten
        context['anzeige'] = "Bitte gebe bei Antwort auf deutsches wort 1 die englische Übersetzung von dem Deutschem Wort ein."
        controlle="controlle"
        context['fuer_deutschtest_abschließung'] = controlle
        return context

