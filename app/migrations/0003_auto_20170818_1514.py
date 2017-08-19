# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170815_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', tinymce.models.HTMLField()),
                ('assessment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RenameModel(
            old_name='Case',
            new_name='CaseMaster',
        ),
        migrations.RenameModel(
            old_name='Module',
            new_name='Flag',
        ),
        migrations.AlterModelOptions(
            name='flag',
            options={},
        ),
        migrations.RenameField(
            model_name='flag',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='casemaster',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ModuleMaster'),
        ),
    ]
