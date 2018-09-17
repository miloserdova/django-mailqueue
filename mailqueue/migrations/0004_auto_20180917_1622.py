# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-17 13:22
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailqueue', '0003_auto_20150714_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailermessage',
            name='attach',
            field=models.FileField(blank=True, editable=False, null=True, upload_to='attach'),
        ),
        migrations.AlterField(
            model_name='mailermessage',
            name='html_message',
            field=models.TextField(blank=True, default='', verbose_name='html message'),
        ),
    ]
