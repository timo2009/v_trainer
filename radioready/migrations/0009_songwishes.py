# Generated by Django 3.1.1 on 2021-06-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioready', '0008_auto_20210604_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongWishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_wishes', models.URLField()),
                ('author', models.CharField(blank=True, default='', max_length=1000)),
            ],
        ),
    ]