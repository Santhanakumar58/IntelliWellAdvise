# Generated by Django 5.0.1 on 2024-02-13 23:49

import obrecordedlogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OBRecordedLogsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obfgId', models.PositiveIntegerField()),
                ('obwellid', models.PositiveIntegerField()),
                ('obsurvey_Date', models.DateField()),
                ('obhole_size', models.CharField(choices=[('26_inch', '26_inch'), ('20_inch', '20_inch'), ('16_inch', '16_inch'), ('12_1/4_inch', '12_1/4_inch'), ('8_1/2_inch', '8_1/2_inch'), ('6_1/8_inch', '6_1/8_inch'), ('4_1/2_inch', '4_1/2_inch')], default='12_1/4_inch', max_length=50)),
                ('oblog_Type', models.CharField(choices=[('LWD', 'LWD'), ('MWD', 'MWD'), ('Open_Hole', 'Open_Hole'), ('Cased_Hole', 'Cased_Hole')], default='Open_Hole', max_length=50)),
                ('obtool_string', models.CharField(max_length=100)),
                ('obfrom_MD', models.FloatField()),
                ('obto_MD', models.FloatField()),
                ('observice_Provider', models.CharField(blank=True, max_length=50, null=True)),
                ('obunit_name', models.CharField(blank=True, max_length=50, null=True)),
                ('obanalyst', models.CharField(blank=True, max_length=30, null=True)),
                ('obinterpretation', models.TextField()),
                ('oblogImage', models.ImageField(blank=True, null=True, upload_to=obrecordedlogs.models.filepath)),
                ('obremarks', models.CharField(max_length=100)),
                ('obfile_type', models.CharField(choices=[('LAS', 'LAS'), ('CSV', 'CSV'), ('DLIS', 'DLIS')], default='LAS', max_length=50)),
                ('obfile_Name', models.FileField(blank=True, null=True, upload_to=obrecordedlogs.models.filepath)),
            ],
        ),
    ]
