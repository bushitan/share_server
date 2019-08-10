# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': '点赞', 'verbose_name_plural': '点赞'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '人员', 'verbose_name_plural': '人员'},
        ),
        migrations.AddField(
            model_name='score',
            name='helper',
            field=models.ForeignKey(verbose_name='助力的客户', to='photo.User', related_name='helper', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ForeignKey(verbose_name='图片', to='photo.BaseImage', null=True, blank=True),
        ),
    ]
