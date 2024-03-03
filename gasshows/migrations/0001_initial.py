# Generated by Django 4.2.1 on 2023-05-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GasShowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgId', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('formation', models.CharField(max_length=100)),
                ('top_MD', models.FloatField()),
                ('bottom_MD', models.FloatField()),
                ('total_Gas', models.FloatField()),
                ('methane', models.FloatField()),
                ('ethane', models.FloatField()),
                ('propane', models.FloatField()),
                ('iso_Butane', models.FloatField()),
                ('neo_Butane', models.FloatField()),
                ('iso_Pentane', models.FloatField()),
                ('neo_Pentane', models.FloatField()),
                ('remarks', models.CharField(max_length=100)),
            ],
        ),
    ]