from django.contrib import admin

# Register your models here.
from v_trainer.models import DeutschesWort, EnglischesWort, EnglischTestEineVokalel, DeutschTestEineVokalel, LateinTestZehnVokalel, LateinischesWort

admin.site.register(DeutschesWort)
admin.site.register(EnglischesWort)
admin.site.register(LateinischesWort)


@admin.register(EnglischTestEineVokalel)
class DeutschTest(admin.ModelAdmin):
    list_display = ("id", "user", "englisches_wort_1")\

@admin.register(DeutschTestEineVokalel)
class EnglischTest(admin.ModelAdmin):
    list_display = ("id", "user", "deutsches_wort_1")\

@admin.register(LateinTestZehnVokalel)
class EnglischTest(admin.ModelAdmin):
    list_display = ("id", "user", "lateinisches_wort_1", "lateinisches_wort_2", "lateinisches_wort_3", "lateinisches_wort_4", "lateinisches_wort_5", "lateinisches_wort_6", "lateinisches_wort_7", "lateinisches_wort_8", "lateinisches_wort_9", "lateinisches_wort_10")

