# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0007_auto_20190731_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-sn'], 'verbose_name_plural': '文章', 'verbose_name': '文章'},
        ),
        migrations.AddField(
            model_name='article',
            name='sn',
            field=models.IntegerField(verbose_name='排序', default=0),
        ),
    ]
