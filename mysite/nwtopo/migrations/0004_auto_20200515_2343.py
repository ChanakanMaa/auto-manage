# Generated by Django 3.0.5 on 2020-05-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nwtopo', '0003_remove_template_temp_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deploy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('temp_amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='template',
            old_name='title',
            new_name='temp_name',
        ),
        migrations.RemoveField(
            model_name='template',
            name='temp_amount',
        ),
    ]