# Generated by Django 4.0.5 on 2022-07-01 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drillingwelldata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drillingwelldata',
            name='lattitude',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='drillingwelldata',
            name='longitude',
            field=models.CharField(max_length=20),
        ),
    ]
