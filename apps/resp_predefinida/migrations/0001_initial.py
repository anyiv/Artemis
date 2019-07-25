# Generated by Django 2.2.2 on 2019-07-25 21:50

import apps.resp_predefinida.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RespuestaPredefinida',
            fields=[
                ('codRespuestaP', models.CharField(default=apps.resp_predefinida.models.RespuestaPredefinida.codRespuestaP, max_length=8, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=500)),
                ('categoria', models.CharField(choices=[('pet', 'Petición'), ('que', 'Queja'), ('rec', 'Reclamo'), ('sug', 'Sugerencia')], max_length=20)),
                ('contUso', models.IntegerField(default=0)),
                ('estatus', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
            ],
        ),
    ]
