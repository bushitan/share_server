# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_user_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='photo',
            new_name='phone',
        ),
    ]
