# Generated by Django 2.2.4 on 2019-09-03 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20190903_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalresponse',
            name='datetime_create',
        ),
        migrations.RemoveField(
            model_name='historicalresponse',
            name='datetime_update',
        ),
        migrations.RemoveField(
            model_name='historicalsurvey',
            name='datetime_create',
        ),
        migrations.RemoveField(
            model_name='historicalsurvey',
            name='datetime_update',
        ),
        migrations.RemoveField(
            model_name='response',
            name='datetime_create',
        ),
        migrations.RemoveField(
            model_name='response',
            name='datetime_update',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='datetime_create',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='datetime_update',
        ),
    ]
