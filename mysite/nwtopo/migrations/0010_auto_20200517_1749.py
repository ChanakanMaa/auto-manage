# Generated by Django 3.0.5 on 2020-05-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nwtopo', '0009_auto_20200517_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deploy',
            name='date_time',
        ),
        migrations.AddField(
            model_name='deploy',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
