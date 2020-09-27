from django.contrib import admin

# Register your models here.
from v_trainer.models import DeutschesWort, EnglischesWort, DeutschTest

admin.site.register(DeutschesWort)
admin.site.register(EnglischesWort)


@admin.register(DeutschTest)
class DeutschTest(admin.ModelAdmin):
    list_display = ("id", "user")
