from django.contrib import admin

# Register your models here.
from radioready.models import RadioShow, RadioUser


@admin.register(RadioShow)
class RadioShow(admin.ModelAdmin):
    list_display = ("id", "name", "link_to_radio_show", "quiz")

@admin.register(RadioUser)
class RadioShow(admin.ModelAdmin):
    list_display = ("id", "firstname", "username", "passwort")
