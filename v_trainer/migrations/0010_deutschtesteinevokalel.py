# Generated by Django 3.1.1 on 2021-05-01 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v_trainer', '0009_delete_deutschtest'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeutschTestEineVokalel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antwort_deutsches_wort_1', models.CharField(blank=True, max_length=120, null=True)),
                ('deutsches_wort_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deutsch_test_wort_1', to='v_trainer.deutscheswort')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
