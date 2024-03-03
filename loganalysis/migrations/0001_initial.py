# Generated by Django 4.2.1 on 2023-05-24 04:47

from django.db import migrations, models
import loganalysis.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogAnalysisModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fgid', models.PositiveIntegerField()),
                ('wellid', models.PositiveIntegerField()),
                ('casingSize', models.CharField(choices=[('4', '4'), ('4 1/2', '4 1/2'), ('5', '5'), ('5 1/2', '5 1/2'), ('6 5/8', '6 5/8'), ('7', '7'), ('7 5/8', '7 5/8'), ('7 3/4', '7 3/4'), ('8 5/8', '8 5/8'), ('9 5/8', '9 5/8'), ('10 3/4', '10 3/3'), ('11 3/4', '11 3/3'), ('13 3/8', '13 3/8'), ('16', '16'), ('18 5/8', '18 5/8'), ('20', '20')], default='7', max_length=50)),
                ('analyst', models.CharField(max_length=30)),
                ('recorded_date', models.DateField()),
                ('interpretation', models.TextField()),
                ('logImage', models.ImageField(blank=True, null=True, upload_to=loganalysis.models.filepath)),
                ('remarks', models.CharField(max_length=100)),
            ],
        ),
    ]