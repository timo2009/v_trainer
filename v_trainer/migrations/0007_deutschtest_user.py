# Generated by Django 3.1.1 on 2020-09-27 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v_trainer', '0006_auto_20200927_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='deutschtest',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]