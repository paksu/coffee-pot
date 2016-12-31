# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-31 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0002_auto_20161026_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelCombination',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, verbose_name='Unique identifier')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date/time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last update date/time')),
                ('description', models.TextField(help_text='What these two labels would be described together?', verbose_name='Description')),
                ('left_label', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='recognition.Label', verbose_name='Left-side label')),
                ('right_label', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='recognition.Label', verbose_name='Right-side label')),
            ],
            options={
                'ordering': ['left_label__order', 'right_label__order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='labelcombination',
            unique_together=set([('left_label', 'right_label')]),
        ),
    ]
