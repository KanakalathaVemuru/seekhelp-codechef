# Generated by Django 2.1.1 on 2018-09-16 07:08

import div.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rrid', models.IntegerField(verbose_name=div.models.SendRequest)),
                ('funame', models.CharField(max_length=50)),
                ('tname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReplyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rerid', models.IntegerField(verbose_name=div.models.SendRequest)),
                ('funame', models.CharField(max_length=50)),
                ('tuname', models.CharField(max_length=50)),
                ('suggestion', models.TextField()),
                ('retime', models.TimeField(auto_now_add=True)),
                ('date', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SendRequest',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=50)),
                ('problemcode', models.CharField(max_length=50)),
                ('languageused', models.CharField(max_length=10)),
                ('question', models.TextField()),
                ('description', models.TextField()),
                ('codesnapshot', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
