from django.db import models


# Create your models here.
class RadioShow(models.Model):
    name = models.CharField(max_length=100, default='')
    link_to_radio_show = models.URLField()
    quiz = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.name
