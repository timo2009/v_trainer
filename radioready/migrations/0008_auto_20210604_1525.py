# Generated by Django 3.1.1 on 2021-06-04 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radioready', '0007_radioshow_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radioshow',
            options={'ordering': ['-created']},
        ),
    ]
