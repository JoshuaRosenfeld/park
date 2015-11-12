# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0003_instance_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='lat',
            field=models.DecimalField(default=None, max_digits=9, decimal_places=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spot',
            name='lng',
            field=models.DecimalField(default=None, max_digits=9, decimal_places=6),
            preserve_default=False,
        ),
    ]
