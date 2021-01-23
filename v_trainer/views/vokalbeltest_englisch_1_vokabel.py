from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from v_trainer.models import EnglischTestEineVokalel
from django.urls import reverse_lazy


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
