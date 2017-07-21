# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20170720_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API.TicketStatus', verbose_name='Ticket status'),
        ),
    ]
