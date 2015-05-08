# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import builtins


class Migration(migrations.Migration):

    dependencies = [
        ('dade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('accounts', models.ManyToManyField(to='dade.Account', verbose_name='Accounts')),
                ('groupschool', models.ForeignKey(to='dade.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('notifytype', models.CharField(verbose_name=builtins.max, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
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
        migrations.RenameField(
            model_name='account',
            old_name='school',
            new_name='accountschool',
        ),
        migrations.AddField(
            model_name='school',
            name='groups',
            field=models.ManyToManyField(to='dade.Group', verbose_name='Groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='school',
            name='schoolaccounts',
            field=models.ManyToManyField(to='dade.Account', verbose_name='Accounts'),
            preserve_default=True,
        ),
    ]
