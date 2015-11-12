# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0005_auto_20151111_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='residence',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=-1, max_digits=9),
        ),
        migrations.AddField(
            model_name='residence',
            name='lng',
            field=models.DecimalField(decimal_places=6, default=-1, max_digits=9),
        ),
    ]
