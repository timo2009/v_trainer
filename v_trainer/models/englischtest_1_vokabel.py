from django.db import models
from v_trainer import models as v_models
from django.contrib.auth.models import User


class EnglischTestEineVokalel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    englisches_wort_1 = models.ForeignKey(v_models.EnglischesWort, related_name='englisch_test_wort_1', on_delete=models.PROTECT)
    antwort_englisches_wort_1 = models.CharField(null=True, blank=True, max_length=120)
