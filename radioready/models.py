from django.db import models


# Create your models here.
class RadioShow(models.Model):
    name = models.CharField(max_length=100, default='')
    link_to_radio_show = models.URLField()
    quiz = models.CharField(max_length=1000, default='', blank=True)
    einsendeschluss = models.CharFieldField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.name

class RadioUser(models.Model):
    firstname = models.CharField(max_length=1000, default='', blank=True)
    username = models.CharField(max_length=100, default='')
    passwort = models.CharField(max_length=100, default='')



    def __str__(self):
        return self.firstname


