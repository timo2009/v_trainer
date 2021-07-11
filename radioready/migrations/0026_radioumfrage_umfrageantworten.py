# Generated by Django 3.1.1 on 2021-07-11 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radioready', '0025_auto_20210704_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='UmfrageAntworten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antwort', models.CharField(max_length=100, unique=True, verbose_name='Antwort')),
            ],
        ),
        migrations.CreateModel(
            name='RadioUmfrage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(default='', max_length=100, verbose_name='Frage:')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deutsches_wort_1', to='radioready.umfrageantworten', verbose_name='Deine Antwort:')),
            ],
        ),
    ]
