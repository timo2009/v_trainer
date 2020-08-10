from django.db import models
from v_trainer.models import EnglischesWort


# Create your models here.
class DeutschesWort(models.Model):
    wort = models.CharField(max_length=100)
    ewort = models.ManyToManyField(EnglischesWort)

    def __str__(self):
        return self.wort


#TODO Engliches Wort Problem lösen