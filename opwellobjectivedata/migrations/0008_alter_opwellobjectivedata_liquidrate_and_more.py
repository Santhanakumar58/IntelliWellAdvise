# Generated by Django 4.2.1 on 2023-05-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opwellobjectivedata', '0007_remove_opwellobjectivedata_gasrate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opwellobjectivedata',
            name='liquidrate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opwellobjectivedata',
            name='watercut',
            field=models.FloatField(blank=True, null=True),
        ),
    ]