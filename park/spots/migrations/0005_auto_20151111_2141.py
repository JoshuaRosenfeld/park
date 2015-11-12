# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0004_auto_20151111_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='lng',
        ),
    ]
