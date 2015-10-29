# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('rate', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=140)),
                ('residence', models.ForeignKey(to='spots.Residence')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('cost', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('nickname', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='guest',
            field=models.ForeignKey(to='spots.User'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='instance',
            field=models.ForeignKey(to='spots.Instance'),
        ),
        migrations.AddField(
            model_name='residence',
            name='user',
            field=models.ForeignKey(to='spots.User'),
        ),
        migrations.AddField(
            model_name='instance',
            name='spot',
            field=models.ForeignKey(to='spots.Spot'),
        ),
    ]
