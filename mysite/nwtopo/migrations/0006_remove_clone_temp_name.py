# Generated by Django 3.0.5 on 2020-05-16 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nwtopo', '0005_clone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clone',
            name='temp_name',
        ),
    ]
