# Generated by Django 3.1.1 on 2021-06-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioready', '0013_delete_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioshow',
            name='quiz',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
