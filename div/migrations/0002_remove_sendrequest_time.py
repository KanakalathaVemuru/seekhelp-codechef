# Generated by Django 2.1.1 on 2018-09-16 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('div', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendrequest',
            name='time',
        ),
    ]
