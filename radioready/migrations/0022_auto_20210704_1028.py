# Generated by Django 3.1.1 on 2021-07-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioready', '0021_radioshow_hide_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioshow',
            name='hide_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
