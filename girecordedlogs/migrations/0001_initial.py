# Generated by Django 5.0.1 on 2024-02-13 23:49

import girecordedlogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GIRecordedLogsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gifgId', models.PositiveIntegerField()),
                ('giwellid', models.PositiveIntegerField()),
                ('gisurvey_Date', models.DateField()),
                ('gihole_size', models.CharField(choices=[('26_inch', '26_inch'), ('20_inch', '20_inch'), ('16_inch', '16_inch'), ('12_1/4_inch', '12_1/4_inch'), ('8_1/2_inch', '8_1/2_inch'), ('6_1/8_inch', '6_1/8_inch'), ('4_1/2_inch', '4_1/2_inch')], default='12_1/4_inch', max_length=50)),
                ('gilog_Type', models.CharField(choices=[('LWD', 'LWD'), ('MWD', 'MWD'), ('Open_Hole', 'Open_Hole'), ('Cased_Hole', 'Cased_Hole')], default='Open_Hole', max_length=50)),
                ('gitool_string', models.CharField(max_length=100)),
                ('gifrom_MD', models.FloatField()),
                ('gito_MD', models.FloatField()),
                ('giservice_Provider', models.CharField(blank=True, max_length=50, null=True)),
                ('giunit_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gianalyst', models.CharField(blank=True, max_length=30, null=True)),
                ('giinterpretation', models.TextField()),
                ('gilogImage', models.ImageField(blank=True, null=True, upload_to=girecordedlogs.models.filepath)),
                ('giremarks', models.CharField(max_length=100)),
                ('gifile_type', models.CharField(choices=[('LAS', 'LAS'), ('CSV', 'CSV'), ('DLIS', 'DLIS')], default='LAS', max_length=50)),
                ('gifile_Name', models.FileField(blank=True, null=True, upload_to=girecordedlogs.models.filepath)),
            ],
        ),
    ]
