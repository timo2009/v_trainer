from django.db import models


# Create your models here.
class DeutschesWort(models.Model):
    wort = models.CharField(max_length=100)

    def __str__(self):
        return self.wort
