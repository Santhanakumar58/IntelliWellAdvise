# Generated by Django 5.0.1 on 2024-02-09 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WIDeviationsurveydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifgId', models.PositiveIntegerField()),
                ('wiwellid', models.PositiveIntegerField()),
                ('wimeasuredDepth', models.FloatField()),
                ('wiangle', models.FloatField()),
                ('wiazimuth', models.FloatField()),
                ('witvd', models.FloatField(blank=True, null=True)),
                ('winorthSouth', models.FloatField(blank=True, null=True)),
                ('wieastWest', models.FloatField(blank=True, null=True)),
                ('winetDrift', models.FloatField(blank=True, null=True)),
                ('winetDirection', models.FloatField(blank=True, null=True)),
                ('wiverticalSection', models.FloatField(blank=True, null=True)),
                ('widogLeg', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
