# Generated by Django 3.1.1 on 2021-07-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioready', '0019_auto_20210619_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='radioshow',
            name='staffel',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]