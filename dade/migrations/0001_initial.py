# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('realname', models.CharField(max_length=256)),
                ('priviledge', models.IntegerField(default=1)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('confirmation_code', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('accounts', models.ManyToManyField(to='dade.Account', verbose_name=b'Accounts')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notifytype', models.CharField(max_length=128, verbose_name=__builtin__.max)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('groups', models.ManyToManyField(to='dade.Group', verbose_name=b'Groups')),
                ('schoolaccounts', models.ManyToManyField(to='dade.Account', verbose_name=b'Accounts')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='groupschool',
            field=models.ForeignKey(to='dade.School'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='group',
            field=models.ForeignKey(to='dade.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='school',
            field=models.ForeignKey(to='dade.School'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='accountschool',
            field=models.ForeignKey(to='dade.School'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
