# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20190725_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(to='photo.Tag', blank=True, null=True, verbose_name='标签'),
        ),
    ]
