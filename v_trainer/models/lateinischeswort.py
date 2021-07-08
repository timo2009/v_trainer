
from django.db import models
from v_trainer import models as v_models


class LateinischesWort(models.Model):
    wort = models.CharField(max_length=100, verbose_name='Wort', unique=True)
    dwort = models.ManyToManyField(v_models.DeutschesWort, related_name='list_of_deutschewords')




    def __str__(self):
        return self.wort
