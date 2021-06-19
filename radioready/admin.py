from django.contrib import admin
from django.shortcuts import get_object_or_404

# Register your models here.
from radioready.models import RadioShow, SongWishes


@admin.register(RadioShow)
class RadioShow(admin.ModelAdmin):
    list_display = ("id", "name", "link_to_radio_show", "quiz", "deadline")


@admin.register(SongWishes)
class SongWishes(admin.ModelAdmin):
    list_display = ("id", "author", "song", "created", "creator")

    def save_model(self, request, obj, form, change):
        print("#########request.user############")
        print(request.user)
        print("request.user.id")
        print(request.user.id)
        if getattr(obj, 'user', None) is None:
            obj.creator = request.user
        obj.save()
