# Generated by Django 2.2.2 on 2019-07-27 03:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqs', '0003_auto_20190726_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqs',
            name='fechaFinalizado',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pqs',
            name='fechaRegistro',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
