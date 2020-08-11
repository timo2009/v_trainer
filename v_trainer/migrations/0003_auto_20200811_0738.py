# Generated by Django 3.1 on 2020-08-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_trainer', '0002_englischeswort_dwort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deutscheswort',
            name='wort',
            field=models.CharField(max_length=100, verbose_name='dwort'),
        ),
        migrations.AlterField(
            model_name='englischeswort',
            name='dwort',
            field=models.ManyToManyField(related_name='list_of_dwords', to='v_trainer.DeutschesWort'),
        ),
        migrations.AlterField(
            model_name='englischeswort',
            name='wort',
            field=models.CharField(max_length=100, verbose_name='ewort'),
        ),
    ]
