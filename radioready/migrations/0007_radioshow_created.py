# Generated by Django 3.1.1 on 2021-06-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioready', '0006_auto_20210604_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='radioshow',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
