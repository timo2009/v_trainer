from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from v_trainer.models import LateinTestZehnVokalel, DeutschesWort, LateinischesWort
from django.urls import reverse_lazy
from django.utils import timezone



class LateinTestZehnVokalelCreate(CreateView):
    model = LateinTestZehnVokalel
    fields = ['user', 'lateinisches_wort_1', 'lateinisches_wort_2', 'lateinisches_wort_3', 'lateinisches_wort_4', 'lateinisches_wort_5', 'lateinisches_wort_6', 'lateinisches_wort_7', 'lateinisches_wort_8', 'lateinisches_wort_9', 'lateinisches_wort_10']
    success_url = reverse_lazy('lateintest_10_vokabel_list')



class LateinTestZehnVokalelUpdate(UpdateView):
    model = LateinTestZehnVokalel
    fields = ['user', 'lateinisches_wort_1', 'antwort_lateinisches_wort_1', 'lateinisches_wort_2', 'antwort_lateinisches_wort_2', 'lateinisches_wort_3', 'antwort_lateinisches_wort_3', 'lateinisches_wort_4', 'antwort_lateinisches_wort_4', 'lateinisches_wort_5', 'antwort_lateinisches_wort_5', 'lateinisches_wort_6', 'antwort_lateinisches_wort_6', 'lateinisches_wort_7', 'antwort_lateinisches_wort_7', 'lateinisches_wort_8', 'antwort_lateinisches_wort_8', 'lateinisches_wort_9', 'antwort_lateinisches_wort_9', 'lateinisches_wort_10', 'antwort_lateinisches_wort_10']
    success_url = reverse_lazy('lateintest_10_vokabel_list')


class LateinTestZehnVokalelList(ListView):
    model = LateinTestZehnVokalel


class LateinTestZehnVokalelDetail(DetailView):
    model = LateinTestZehnVokalel


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Hiermit hole ich mir das zu dem Lateintest gehörende lateinisches Wort
        lateinisches_wort_1 = self.object.lateinisches_wort_1
        lateinisches_wort_2 = self.object.lateinisches_wort_2
        lateinisches_wort_3 = self.object.lateinisches_wort_3
        lateinisches_wort_4 = self.object.lateinisches_wort_4
        lateinisches_wort_5 = self.object.lateinisches_wort_5
        lateinisches_wort_6 = self.object.lateinisches_wort_6
        lateinisches_wort_7 = self.object.lateinisches_wort_7
        lateinisches_wort_8 = self.object.lateinisches_wort_8
        lateinisches_wort_9 = self.object.lateinisches_wort_9
        lateinisches_wort_10 = self.object.lateinisches_wort_10



        context['lateinisches_wort_1'] = lateinisches_wort_1
        context['deutsche_woerter_1'] = lateinisches_wort_1.dwort.all()

        context['lateinisches_wort_2'] = lateinisches_wort_2
        context['deutsche_woerter_2'] = lateinisches_wort_2.dwort.all()

        context['lateinisches_wort_3'] = lateinisches_wort_3
        context['deutsche_woerter_3'] = lateinisches_wort_3.dwort.all()

        context['lateinisches_wort_4'] = lateinisches_wort_4
        context['deutsche_woerter_4'] = lateinisches_wort_4.dwort.all()

        context['lateinisches_wort_5'] = lateinisches_wort_5
        context['deutsche_woerter_5'] = lateinisches_wort_5.dwort.all()

        context['lateinisches_wort_6'] = lateinisches_wort_6
        context['deutsche_woerter_6'] = lateinisches_wort_6.dwort.all()

        context['lateinisches_wort_7'] = lateinisches_wort_7
        context['deutsche_woerter_7'] = lateinisches_wort_7.dwort.all()

        context['lateinisches_wort_8'] = lateinisches_wort_8
        context['deutsche_woerter_8'] = lateinisches_wort_8.dwort.all()

        context['lateinisches_wort_9'] = lateinisches_wort_9
        context['deutsche_woerter_9'] = lateinisches_wort_9.dwort.all()

        context['lateinisches_wort_10'] = lateinisches_wort_10
        context['deutsche_woerter_10'] = lateinisches_wort_10.dwort.all()

        ergebnis_1 = 'falsch'
        ergebnis_2 = 'falsch'
        ergebnis_3 = 'falsch'
        ergebnis_4 = 'falsch'
        ergebnis_5 = 'falsch'
        ergebnis_6 = 'falsch'
        ergebnis_7 = 'falsch'
        ergebnis_8 = 'falsch'
        ergebnis_9 = 'falsch'
        ergebnis_10 = 'falsch'
        punkte = 0
        for wort in lateinisches_wort_1.dwort.all():

            if wort.wort == self.object.antwort_lateinisches_wort_1:
                ergebnis_1 = 'richtig'
                punkte=punkte+1
            context['ergebnis_1'] = ergebnis_1


        for wort in lateinisches_wort_2.dwort.all():

            if wort.wort == self.object.antwort_lateinisches_wort_2:
                ergebnis_2 = 'richtig'
                punkte=punkte+1

            context['ergebnis_2'] = ergebnis_2


        for wort in lateinisches_wort_3.dwort.all():

            if wort.wort == self.object.antwort_lateinisches_wort_3:
                ergebnis_3 = 'richtig'
                punkte=punkte+1

            context['ergebnis_3'] = ergebnis_3

        for wort in lateinisches_wort_4.dwort.all():

            if wort.wort == self.object.antwort_lateinisches_wort_4:
                ergebnis_4 = 'richtig'
                punkte=punkte+1

            context['ergebnis_4'] = ergebnis_4


        for wort in lateinisches_wort_5.dwort.all():

            if wort.wort == self.object.antwort_lateinisches_wort_5:
                ergebnis_5 = 'richtig'
                punkte=punkte+1

            context['ergebnis_5'] = ergebnis_5


        for wort in lateinisches_wort_6.dwort.all():

            if wort.wort == self.object.antwort_lateinisches_wort_6:
                ergebnis_6 = 'richtig'
                punkte=punkte+1

            context['ergebnis_6'] = ergebnis_6

        for wort in lateinisches_wort_7.dwort.all():

            if wort.wort == self.object.antwort_lateinisches_wort_7:
                ergebnis_7 = 'richtig'
                punkte=punkte+1

            context['ergebnis_7'] = ergebnis_7


        for wort in lateinisches_wort_8.dwort.all():

            if wort.wort == self.object.antwort_lateinisches_wort_8:
                ergebnis_8 = 'richtig'
                punkte=punkte+1

            context['ergebnis_8'] = ergebnis_8


        for wort in lateinisches_wort_9.dwort.all():

            if wort.wort == self.object.antwort_lateinisches_wort_9:
                ergebnis_9 = 'richtig'
                punkte=punkte+1

            context['ergebnis_9'] = ergebnis_9

        for wort in lateinisches_wort_10.dwort.all():

            if wort.wort == self.object.antwort_lateinisches_wort_10:
                ergebnis_10 = 'richtig'
                punkte=punkte+1

            context['ergebnis_10'] = ergebnis_10
            context['punkte'] = punkte
        return context
