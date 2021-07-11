from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
import radioready


class RadioShow(models.Model):
    name = models.CharField(max_length=100, default='')
    link_to_radio_show = models.URLField()
    quiz = models.TextField(max_length=1000, default='', blank=True)
    winner = models.CharField(max_length=1000, default='', blank=True)
    staffel = models.CharField(max_length=1000, default='', blank=True)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    hide_until = models.CharField(max_length=1000, default='', blank=True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class SongWishes(models.Model):
    author = models.CharField(max_length=100)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    song = models.CharField(null=True, max_length=1000)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.creator = request.user
        obj.save()

    class Meta:
        ordering = ['-created']

class Kommentare(models.Model):
    kommentar = models.TextField(max_length=1000, default='', blank=True, verbose_name="Dein Kommentar:")
    kommentar_antwort = models.TextField(max_length=1000, default='', blank=True, verbose_name="Die Antwort zu dem Kommentar:")
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


