from django.db import models


# Create your models here.
class RadioShow(models.Model):
    name = models.CharField(max_length=100)
    link_to_radio_show = models.URLField()

    def __str__(self):
        return self.name
