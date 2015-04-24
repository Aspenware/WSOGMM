# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('realname', models.CharField(max_length=256)),
                ('priviledge', models.IntegerField(default=1)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('confirmation_code', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='school',
            field=models.ForeignKey(to='dade.School'),
        ),
    ]
