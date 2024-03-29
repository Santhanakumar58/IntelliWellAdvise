# Generated by Django 5.0.1 on 2024-02-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GIGasShowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gifgId', models.PositiveIntegerField()),
                ('giwellid', models.PositiveIntegerField()),
                ('giformation', models.CharField(max_length=100)),
                ('gitop_MD', models.FloatField()),
                ('gibottom_MD', models.FloatField()),
                ('gitotal_Gas', models.FloatField()),
                ('gimethane', models.FloatField()),
                ('giethane', models.FloatField()),
                ('gipropane', models.FloatField()),
                ('giiso_Butane', models.FloatField()),
                ('gineo_Butane', models.FloatField()),
                ('giiso_Pentane', models.FloatField()),
                ('gineo_Pentane', models.FloatField()),
                ('giremarks', models.CharField(max_length=100)),
            ],
        ),
    ]
