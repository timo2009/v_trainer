from django.db import models
from v_trainer import models as v_models
from django.contrib.auth.models import User


class DeutschTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fehler = models.PositiveIntegerField(verbose_name='fehler', blank=True, null=True)
    dwort = models.ManyToManyField(v_models.DeutschesWort, related_name='deutsch_test_woerter')
