from django.contrib import admin
from django.shortcuts import get_object_or_404

# Register your models here.
from radioready.models import RadioShow, SongWishes, Kommentare


@admin.register(RadioShow)
class RadioShow(admin.ModelAdmin):
    list_display = ("id", "name", "link_to_radio_show", "quiz", "deadline", "staffel")


@admin.register(SongWishes)
class SongWishes(admin.ModelAdmin):
    list_display = ("id", "author", "song", "created", "creator")\

@admin.register(Kommentare)
class Kommentare(admin.ModelAdmin):
    list_display = ("id", "kommentar", "kommentar_antwort", "creator")
