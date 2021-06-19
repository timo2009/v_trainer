from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RadioShow(models.Model):
    name = models.CharField(max_length=100, default='')
    link_to_radio_show = models.URLField()
    quiz = models.TextField(max_length=1000, default='', blank=True)
    winner = models.CharField(max_length=1000, default='', blank=True)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class SongWishes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    song_wishes = models.CharField(max_length=100),
    author = models.CharField(max_length=1000)

    def __str__(self):
        return self.song_wishes

