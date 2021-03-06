# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-29 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0002_auto_20161026_1854'),
        ('webcam', '0002_picture_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='left_label',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='left_pictures', to='recognition.Label', verbose_name='Left-side label'),
        ),
        migrations.AddField(
            model_name='picture',
            name='right_label',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='right_pictures', to='recognition.Label', verbose_name='Right-side label'),
        ),
        migrations.AlterIndexTogether(
            name='picture',
            index_together=set([('right_label', 'created_at'), ('left_label', 'created_at')]),
        ),
    ]
