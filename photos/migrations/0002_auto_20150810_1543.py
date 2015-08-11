# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='user',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='image',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='image',
            name='created',
        ),
        migrations.RemoveField(
            model_name='image',
            name='height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width',
        ),
        migrations.AddField(
            model_name='image',
            name='descripcion',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='image',
            name='imagen',
            field=models.CharField(default=b'', max_length=5000),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
