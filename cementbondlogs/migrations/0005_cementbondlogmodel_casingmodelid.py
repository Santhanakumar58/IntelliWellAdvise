# Generated by Django 5.0.1 on 2024-03-17 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cementbondlogs', '0004_alter_cementbondlogmodel_cblimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cementbondlogmodel',
            name='casingModelid',
            field=models.PositiveBigIntegerField(default=34),
            preserve_default=False,
        ),
    ]
