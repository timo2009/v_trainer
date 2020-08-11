from django.db import models


class DeutschesWort(models.Model):
    wort = models.CharField(max_length=100, verbose_name='dwort')

    def __str__(self):
        return self.wort
