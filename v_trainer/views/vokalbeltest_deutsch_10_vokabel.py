from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from v_trainer.models.deutschtest_10_vokabel import DeutschTestZehnVokalel
from django.urls import reverse_lazy
from django.utils import timezone


class DeutschTestZehnVokalelCreate(CreateView):
    model = DeutschTestZehnVokalel
    fields = ['user', 'deutsches_wort_1', 'deutsches_wort_2', 'deutsches_wort_3', 'deutsches_wort_4',
              'deutsches_wort_5', 'deutsches_wort_6', 'deutsches_wort_7', 'deutsches_wort_8', 'deutsches_wort_9',
              'deutsches_wort_10']
    success_url = reverse_lazy('deutschtest_10_vokabel_list')

    # template_name = 'englischtesteinevokalel_form.html'


class DeutschTestZehnVokaleUpdate(UpdateView):
    model = DeutschTestZehnVokalel
    fields = ['user', 'deutsches_wort_1', 'antwort_auf_deutsches_wort_1', 'deutsches_wort_2',
              'antwort_auf_deutsches_wort_2', 'deutsches_wort_3', 'antwort_auf_deutsches_wort_3', 'deutsches_wort_4',
              'antwort_auf_deutsches_wort_4', 'deutsches_wort_5', 'antwort_auf_deutsches_wort_5', 'deutsches_wort_6',
              'antwort_auf_deutsches_wort_6', 'deutsches_wort_7', 'antwort_auf_deutsches_wort_7', 'deutsches_wort_8',
              'antwort_auf_deutsches_wort_8', 'deutsches_wort_9', 'antwort_auf_deutsches_wort_9', 'deutsches_wort_10',
              'antwort_auf_deutsches_wort_10']
    success_url = reverse_lazy('deutschtest_10_vokabel_list')
    # template_name = 'englisch_test_update_form'


class DeutschTestZehnVokaleList(ListView):
    model = DeutschTestZehnVokalel


class DeutschTestZehnVokaleDetail(DetailView):
    model = DeutschTestZehnVokalel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Hiermit hole ich mir das zu dem Deutschtest gehörende englische Wort

        deutsches_wort_1 = self.object.deutsches_wort_1
        deutsches_wort_2 = self.object.deutsches_wort_2
        deutsches_wort_3 = self.object.deutsches_wort_3
        deutsches_wort_4 = self.object.deutsches_wort_4
        deutsches_wort_5 = self.object.deutsches_wort_5
        deutsches_wort_6 = self.object.deutsches_wort_6
        deutsches_wort_7 = self.object.deutsches_wort_7
        deutsches_wort_8 = self.object.deutsches_wort_8
        deutsches_wort_9 = self.object.deutsches_wort_9
        deutsches_wort_10 = self.object.deutsches_wort_10

        antwort_auf_deutsches_wort_1 = self.object.antwort_auf_deutsches_wort_1
        antwort_auf_deutsches_wort_2 = self.object.antwort_auf_deutsches_wort_2
        antwort_auf_deutsches_wort_3 = self.object.antwort_auf_deutsches_wort_3
        antwort_auf_deutsches_wort_4 = self.object.antwort_auf_deutsches_wort_4
        antwort_auf_deutsches_wort_5 = self.object.antwort_auf_deutsches_wort_5
        antwort_auf_deutsches_wort_6 = self.object.antwort_auf_deutsches_wort_6
        antwort_auf_deutsches_wort_7 = self.object.antwort_auf_deutsches_wort_7
        antwort_auf_deutsches_wort_8 = self.object.antwort_auf_deutsches_wort_8
        antwort_auf_deutsches_wort_9 = self.object.antwort_auf_deutsches_wort_9
        antwort_auf_deutsches_wort_10 = self.object.antwort_auf_deutsches_wort_10

        context['antwort_deutsches_wort_1'] = antwort_auf_deutsches_wort_1
        context['antwort_deutsches_wort_2'] = antwort_auf_deutsches_wort_2
        context['antwort_deutsches_wort_3'] = antwort_auf_deutsches_wort_3
        context['antwort_deutsches_wort_4'] = antwort_auf_deutsches_wort_4
        context['antwort_deutsches_wort_5'] = antwort_auf_deutsches_wort_5
        context['antwort_deutsches_wort_6'] = antwort_auf_deutsches_wort_6
        context['antwort_deutsches_wort_7'] = antwort_auf_deutsches_wort_7
        context['antwort_deutsches_wort_8'] = antwort_auf_deutsches_wort_8
        context['antwort_deutsches_wort_9'] = antwort_auf_deutsches_wort_9
        context['antwort_deutsches_wort_10'] = antwort_auf_deutsches_wort_10

        context['deutsches_wort_1'] = deutsches_wort_1
        context['deutsches_wort_2'] = deutsches_wort_2
        context['deutsches_wort_3'] = deutsches_wort_3
        context['deutsches_wort_4'] = deutsches_wort_4
        context['deutsches_wort_5'] = deutsches_wort_5
        context['deutsches_wort_6'] = deutsches_wort_6
        context['deutsches_wort_7'] = deutsches_wort_7
        context['deutsches_wort_8'] = deutsches_wort_8
        context['deutsches_wort_9'] = deutsches_wort_9
        context['deutsches_wort_10'] = deutsches_wort_10

        context['moeglische_englischen_antworten_1'] = deutsches_wort_1.list_of_dwords.all()
        context['moeglische_englischen_antworten_2'] = deutsches_wort_2.list_of_dwords.all()
        context['moeglische_englischen_antworten_3'] = deutsches_wort_3.list_of_dwords.all()
        context['moeglische_englischen_antworten_4'] = deutsches_wort_4.list_of_dwords.all()
        context['moeglische_englischen_antworten_5'] = deutsches_wort_5.list_of_dwords.all()
        context['moeglische_englischen_antworten_6'] = deutsches_wort_6.list_of_dwords.all()
        context['moeglische_englischen_antworten_7'] = deutsches_wort_7.list_of_dwords.all()
        context['moeglische_englischen_antworten_8'] = deutsches_wort_8.list_of_dwords.all()
        context['moeglische_englischen_antworten_9'] = deutsches_wort_9.list_of_dwords.all()
        context['moeglische_englischen_antworten_10'] = deutsches_wort_10.list_of_dwords.all()

        ergebnis1 = 'falsch'
        ergebnis2 = 'falsch'
        ergebnis3 = 'falsch'
        ergebnis4 = 'falsch'
        ergebnis5 = 'falsch'
        ergebnis6 = 'falsch'
        ergebnis7 = 'falsch'
        ergebnis8 = 'falsch'
        ergebnis9 = 'falsch'
        ergebnis10 = 'falsch'

        punkte=0
        moeglische_englischen_antworten_1 = deutsches_wort_1.list_of_dwords.all()
        for englische_antwort in moeglische_englischen_antworten_1:

            if antwort_auf_deutsches_wort_1 == englische_antwort.wort:
                ergebnis1 = 'richtig'
                punkte=punkte+1
            else:
                print(str(antwort_auf_deutsches_wort_1) + '!=' + str(englische_antwort.wort))

        moeglische_englischen_antworten_2 = deutsches_wort_2.list_of_dwords.all()

        for englische_antwort in moeglische_englischen_antworten_2:

            if antwort_auf_deutsches_wort_2 == englische_antwort.wort:
                ergebnis2 = 'richtig'
                punkte=punkte+1

            else:
                print(str(antwort_auf_deutsches_wort_2) + '!=' + str(englische_antwort.wort))

        moeglische_englischen_antworten_3 = deutsches_wort_3.list_of_dwords.all()

        for englische_antwort in moeglische_englischen_antworten_3:

            if antwort_auf_deutsches_wort_3 == englische_antwort.wort:
                ergebnis3 = 'richtig'
                punkte=punkte+1

            else:
                print(str(antwort_auf_deutsches_wort_3) + '!=' + str(englische_antwort.wort))

        moeglische_englischen_antworten_4 = deutsches_wort_4.list_of_dwords.all()

        for englische_antwort in moeglische_englischen_antworten_4:

            if antwort_auf_deutsches_wort_4 == englische_antwort.wort:
                ergebnis4 = 'richtig'
                punkte=punkte+1

            else:
                print(str(antwort_auf_deutsches_wort_4) + '!=' + str(englische_antwort.wort))

        moeglische_englischen_antworten_5 = deutsches_wort_5.list_of_dwords.all()

        for englische_antwort in moeglische_englischen_antworten_5:

            if antwort_auf_deutsches_wort_5 == englische_antwort.wort:
                ergebnis5 = 'richtig'
                punkte=punkte+1

            else:
                print(str(antwort_auf_deutsches_wort_5) + '!=' + str(englische_antwort.wort))

        moeglische_englischen_antworten_6 = deutsches_wort_6.list_of_dwords.all()

        for englische_antwort in moeglische_englischen_antworten_6:

            if antwort_auf_deutsches_wort_6 == englische_antwort.wort:
                ergebnis6 = 'richtig'
                punkte=punkte+1

            else:
                print(str(antwort_auf_deutsches_wort_6) + '!=' + str(englische_antwort.wort))

        moeglische_englischen_antworten_7 = deutsches_wort_7.list_of_dwords.all()

        for englische_antwort in moeglische_englischen_antworten_7:

            if antwort_auf_deutsches_wort_7 == englische_antwort.wort:
                ergebnis7 = 'richtig'
                punkte=punkte+1

            else:
                print(str(antwort_auf_deutsches_wort_7) + '!=' + str(englische_antwort.wort))

        moeglische_englischen_antworten_8 = deutsches_wort_8.list_of_dwords.all()

        for englische_antwort in moeglische_englischen_antworten_8:

            if antwort_auf_deutsches_wort_8 == englische_antwort.wort:
                ergebnis8 = 'richtig'
                punkte=punkte+1

            else:
                print(str(antwort_auf_deutsches_wort_8) + '!=' + str(englische_antwort.wort))

        moeglische_englischen_antworten_9 = deutsches_wort_9.list_of_dwords.all()

        for englische_antwort in moeglische_englischen_antworten_9:

            if antwort_auf_deutsches_wort_9 == englische_antwort.wort:
                ergebnis9 = 'richtig'
                punkte=punkte+1

            else:
                print(str(antwort_auf_deutsches_wort_9) + '!=' + str(englische_antwort.wort))

        moeglische_englischen_antworten_10 = deutsches_wort_10.list_of_dwords.all()

        for englische_antwort in moeglische_englischen_antworten_10:

            if antwort_auf_deutsches_wort_10 == englische_antwort.wort:
                ergebnis10 = 'richtig'
                punkte=punkte+1

            else:
                print(str(antwort_auf_deutsches_wort_10) + '!=' + str(englische_antwort.wort))

        context['ergebnis1'] = ergebnis1
        context['ergebnis2'] = ergebnis2
        context['ergebnis3'] = ergebnis3
        context['ergebnis4'] = ergebnis4
        context['ergebnis5'] = ergebnis5
        context['ergebnis6'] = ergebnis6
        context['ergebnis7'] = ergebnis7
        context['ergebnis8'] = ergebnis8
        context['ergebnis9'] = ergebnis9
        context['ergebnis10'] = ergebnis10

        context['punkte'] =punkte


        context['englische_woerter_1'] = moeglische_englischen_antworten_1
        context['englische_woerter_2'] = moeglische_englischen_antworten_2
        context['englische_woerter_3'] = moeglische_englischen_antworten_3
        context['englische_woerter_4'] = moeglische_englischen_antworten_4
        context['englische_woerter_5'] = moeglische_englischen_antworten_5
        context['englische_woerter_6'] = moeglische_englischen_antworten_6
        context['englische_woerter_7'] = moeglische_englischen_antworten_7
        context['englische_woerter_8'] = moeglische_englischen_antworten_8
        context['englische_woerter_9'] = moeglische_englischen_antworten_9
        context['englische_woerter_10'] = moeglische_englischen_antworten_10

        return context
