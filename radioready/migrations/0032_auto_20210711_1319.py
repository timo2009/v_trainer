# Generated by Django 3.1.1 on 2021-07-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioready', '0031_auto_20210711_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kommentare',
            name='kommentar',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='Dein Kommentar:'),
        ),
        migrations.AlterField(
            model_name='kommentare',
            name='kommentar_antwort',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='Die Antwort zu dem Kommentar:'),
        ),
    ]
