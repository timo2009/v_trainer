# Generated by Django 3.1.1 on 2021-07-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioready', '0024_auto_20210704_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioshow',
            name='hide_until',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
