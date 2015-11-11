# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0002_auto_20151111_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='booked',
            field=models.BooleanField(default=False),
        ),
    ]
