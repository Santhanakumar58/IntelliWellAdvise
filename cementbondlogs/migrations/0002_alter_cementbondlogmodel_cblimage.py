# Generated by Django 4.0.5 on 2022-07-10 10:15

import cementbondlogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cementbondlogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cementbondlogmodel',
            name='cblImage',
            field=models.ImageField(blank=True, null=True, upload_to=cementbondlogs.models.filepath),
        ),
    ]