from django.db import models
from v_trainer import models as v_models
from django.contrib.auth.models import User


class DeutschTestEineVokalel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    deutsches_wort_1 = models.ForeignKey(v_models.DeutschesWort, related_name='deutsch_test_wort_1',
                                          on_delete=models.PROTECT)
    antwort_deutsches_wort_1 = models.CharField(null=True, blank=True, max_length=120)
