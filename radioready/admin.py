from django.contrib import admin

# Register your models here.
from radioready.models import RadioShow, SongWishes


@admin.register(RadioShow)
class RadioShow(admin.ModelAdmin):
    list_display = ("id", "name", "link_to_radio_show", "quiz", "deadline")\

@admin.register(SongWishes)
class SongWishes(admin.ModelAdmin):
    list_display = ("id", "user", "song_wishes", "author")\

