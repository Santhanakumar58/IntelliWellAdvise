# Generated by Django 4.2.1 on 2023-05-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OilShowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgId', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('formation', models.CharField(max_length=100)),
                ('top_MD', models.FloatField()),
                ('bottom_MD', models.FloatField()),
                ('sample_Type', models.CharField(max_length=100)),
                ('sample_Description', models.CharField(max_length=500)),
                ('remarks', models.CharField(max_length=100)),
            ],
        ),
    ]
