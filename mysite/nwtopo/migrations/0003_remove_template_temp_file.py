# Generated by Django 3.0.5 on 2020-05-10 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nwtopo', '0002_auto_20200509_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='temp_file',
        ),
    ]