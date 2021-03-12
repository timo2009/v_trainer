from django.contrib import admin

# Register your models here.
from v_trainer.models import DeutschesWort, EnglischesWort, EnglischTestEineVokalel

admin.site.register(DeutschesWort)
admin.site.register(EnglischesWort)


@admin.register(EnglischTestEineVokalel)
class DeutschTest(admin.ModelAdmin):
    list_display = ("id", "user", "englisches_wort_1")

