# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cpf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='rg',
            field=models.IntegerField(),
        ),
    ]
