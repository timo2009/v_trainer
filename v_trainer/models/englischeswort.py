from django.db import models
from v_trainer.models import DeutschesWort


class EnglischesWort(models.Model):
    wort = models.CharField(max_length=100)
    dwort = models.ManyToManyField(DeutschesWort)

    def __str__(self):
        return self.wort
