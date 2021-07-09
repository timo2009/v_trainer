from django.contrib import admin

# Register your models here.
from v_trainer.models import DeutschesWort, EnglischesWort, LateinTestZehnVokalel, LateinischesWort, EnglischTestZehnVokalel, DeutschTestZehnVokalel

admin.site.register(DeutschesWort)
admin.site.register(EnglischesWort)
admin.site.register(LateinischesWort)

@admin.register(LateinTestZehnVokalel)
class LateinTest(admin.ModelAdmin):
    list_display = ("id", "user", "lateinisches_wort_1", "lateinisches_wort_2", "lateinisches_wort_3", "lateinisches_wort_4", "lateinisches_wort_5", "lateinisches_wort_6", "lateinisches_wort_7", "lateinisches_wort_8", "lateinisches_wort_9", "lateinisches_wort_10")

@admin.register(EnglischTestZehnVokalel)
class EnglischTest(admin.ModelAdmin):
    list_display = ("id", "user", "englisches_wort_1", "englisches_wort_2", "englisches_wort_3", "englisches_wort_4", "englisches_wort_5", "englisches_wort_6", "englisches_wort_7", "englisches_wort_8", "englisches_wort_9", "englisches_wort_10")

@admin.register(DeutschTestZehnVokalel)
class EnglischTest(admin.ModelAdmin):
    list_display = ("id", "user", "deutsches_wort_1", "deutsches_wort_2", "deutsches_wort_3", "deutsches_wort_4", "deutsches_wort_5", "deutsches_wort_6", "deutsches_wort_7", "deutsches_wort_8", "deutsches_wort_9", "deutsches_wort_10")

