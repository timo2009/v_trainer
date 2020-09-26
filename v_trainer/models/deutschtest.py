from django.db import models
from v_trainer import models as v_models


class DeutschTest(models.Model):
    fehler = models.PositiveIntegerField(verbose_name='fehler')
    dwort = models.ManyToManyField(v_models.DeutschesWort, related_name='deutsch_test_woerter')

    def __str__(self):
        return self.wort
