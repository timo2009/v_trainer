from django.db import models
from v_trainer import models as v_models
from django.contrib.auth.models import User


class LateinTestZehnVokalel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lateinisches_wort_1 = models.ForeignKey(v_models.LateinischesWort, related_name='latein_test_wort_1',

                                          on_delete=models.PROTECT, verbose_name='Zu übersetzendes Wort 1')
    antwort_lateinisches_wort_1 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Übersetzung zu Wort 1')

    lateinisches_wort_2 = models.ForeignKey(v_models.LateinischesWort, related_name='latein_test_wort_2',
                                          on_delete=models.PROTECT, verbose_name='Zu übersetzendes Wort 2')
    antwort_lateinisches_wort_2 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Übersetzung zu Wort 2')

    lateinisches_wort_3 = models.ForeignKey(v_models.LateinischesWort, related_name='latein_test_wort_3',
                                          on_delete=models.PROTECT, verbose_name='Zu übersetzendes Wort 3')
    antwort_lateinisches_wort_3 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Übersetzung zu Wort 3')

    lateinisches_wort_4 = models.ForeignKey(v_models.LateinischesWort, related_name='latein_test_wort_4',
                                          on_delete=models.PROTECT, verbose_name='Zu übersetzendes Wort 4')
    antwort_lateinisches_wort_4 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Übersetzung zu Wort 4')

    lateinisches_wort_5 = models.ForeignKey(v_models.LateinischesWort, related_name='latein_test_wort_5',
                                          on_delete=models.PROTECT, verbose_name='Zu übersetzendes Wort 5')
    antwort_lateinisches_wort_5 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Übersetzung zu Wort 5')

    lateinisches_wort_6 = models.ForeignKey(v_models.LateinischesWort, related_name='latein_test_wort_6',
                                          on_delete=models.PROTECT, verbose_name='Zu übersetzendes Wort 6')
    antwort_lateinisches_wort_6 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Übersetzung zu Wort 6')

    lateinisches_wort_7 = models.ForeignKey(v_models.LateinischesWort, related_name='latein_test_wort_7',
                                          on_delete=models.PROTECT, verbose_name='Zu übersetzendes Wort 7')
    antwort_lateinisches_wort_7 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Übersetzung zu Wort 7')

    lateinisches_wort_8 = models.ForeignKey(v_models.LateinischesWort, related_name='latein_test_wort_8',
                                          on_delete=models.PROTECT, verbose_name='Zu übersetzendes Wort 8')
    antwort_lateinisches_wort_8 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Übersetzung zu Wort 8')

    lateinisches_wort_9 = models.ForeignKey(v_models.LateinischesWort, related_name='latein_test_wort_9',
                                          on_delete=models.PROTECT, verbose_name='Zu übersetzendes Wort 9')
    antwort_lateinisches_wort_9 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Übersetzung zu Wort 9')

    lateinisches_wort_10 = models.ForeignKey(v_models.LateinischesWort, related_name='latein_test_wort_10',
                                          on_delete=models.PROTECT, verbose_name='Zu übersetzendes Wort 10')
    antwort_lateinisches_wort_10 = models.CharField(null=True, blank=True, max_length=120, verbose_name='Übersetzung zu Wort 10')
