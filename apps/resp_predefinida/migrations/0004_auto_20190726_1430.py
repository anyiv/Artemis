# Generated by Django 2.2.2 on 2019-07-26 18:30

import apps.resp_predefinida.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resp_predefinida', '0003_auto_20190726_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestapredefinida',
            name='codRespuestaP',
            field=models.CharField(default=apps.resp_predefinida.models.RespuestaPredefinida.codRespuestaP, max_length=8, primary_key=True, serialize=False),
        ),
    ]