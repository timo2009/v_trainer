from django.contrib import admin

# Register your models here.
from v_trainer.models import DeutschesWort, EnglischesWort, EnglischTestEineVokalel, DeutschTestEineVokalel

admin.site.register(DeutschesWort)
admin.site.register(EnglischesWort)


@admin.register(EnglischTestEineVokalel)
class DeutschTest(admin.ModelAdmin):
    list_display = ("id", "user", "englisches_wort_1")\

@admin.register(DeutschTestEineVokalel)
class EnglischTest(admin.ModelAdmin):
    list_display = ("id", "user", "deutsches_wort_1")

