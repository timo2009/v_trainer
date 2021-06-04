# Generated by Django 3.1.1 on 2021-06-04 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioready', '0002_auto_20210604_0558'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadioUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, default='', max_length=1000)),
                ('username', models.CharField(default='', max_length=100)),
                ('passwort', models.CharField(default='', max_length=100)),
            ],
        ),
    ]