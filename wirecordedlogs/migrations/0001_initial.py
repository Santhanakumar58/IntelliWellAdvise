# Generated by Django 5.0.1 on 2024-02-13 23:49

import wirecordedlogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WIRecordedLogsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifgId', models.PositiveIntegerField()),
                ('wiwellid', models.PositiveIntegerField()),
                ('wisurvey_Date', models.DateField()),
                ('wihole_size', models.CharField(choices=[('26_inch', '26_inch'), ('20_inch', '20_inch'), ('16_inch', '16_inch'), ('12_1/4_inch', '12_1/4_inch'), ('8_1/2_inch', '8_1/2_inch'), ('6_1/8_inch', '6_1/8_inch'), ('4_1/2_inch', '4_1/2_inch')], default='12_1/4_inch', max_length=50)),
                ('wilog_Type', models.CharField(choices=[('LWD', 'LWD'), ('MWD', 'MWD'), ('Open_Hole', 'Open_Hole'), ('Cased_Hole', 'Cased_Hole')], default='Open_Hole', max_length=50)),
                ('witool_string', models.CharField(max_length=100)),
                ('wifrom_MD', models.FloatField()),
                ('wito_MD', models.FloatField()),
                ('wiservice_Provider', models.CharField(blank=True, max_length=50, null=True)),
                ('wiunit_name', models.CharField(blank=True, max_length=50, null=True)),
                ('wianalyst', models.CharField(blank=True, max_length=30, null=True)),
                ('wiinterpretation', models.TextField()),
                ('wilogImage', models.ImageField(blank=True, null=True, upload_to=wirecordedlogs.models.filepath)),
                ('wiremarks', models.CharField(max_length=100)),
                ('wifile_type', models.CharField(choices=[('LAS', 'LAS'), ('CSV', 'CSV'), ('DLIS', 'DLIS')], default='LAS', max_length=50)),
                ('wifile_Name', models.FileField(blank=True, null=True, upload_to=wirecordedlogs.models.filepath)),
            ],
        ),
    ]