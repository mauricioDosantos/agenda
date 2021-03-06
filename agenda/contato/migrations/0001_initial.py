# Generated by Django 3.1.1 on 2020-10-27 19:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('sobrenome', models.CharField(max_length=90)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('data_criacao', models.DateField(default=datetime.date(2020, 10, 27))),
                ('descricao', models.CharField(max_length=400)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contato.categoria')),
            ],
        ),
    ]
