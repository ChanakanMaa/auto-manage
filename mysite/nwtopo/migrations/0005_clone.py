# Generated by Django 3.0.5 on 2020-05-16 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nwtopo', '0004_auto_20200515_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_clone', models.CharField(max_length=100, null=True)),
                ('temp_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nwtopo.Template')),
            ],
        ),
    ]