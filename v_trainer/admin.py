from django.contrib import admin

# Register your models here.
from v_trainer.models import DeutschesWort, EnglischesWort

admin.site.register(DeutschesWort)
admin.site.register(EnglischesWort)