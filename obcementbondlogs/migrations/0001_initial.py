# Generated by Django 5.0.1 on 2024-02-10 08:37

import django.db.models.deletion
import obcementbondlogs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('obcasings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OBCementBondLogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obfgid', models.PositiveIntegerField()),
                ('obwellid', models.PositiveIntegerField()),
                ('obanalyst', models.CharField(max_length=30)),
                ('obrecorded_date', models.DateField()),
                ('obinterpretation', models.TextField()),
                ('obcblImage', models.ImageField(blank=True, null=True, upload_to=obcementbondlogs.models.filepath)),
                ('obcasingSize', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='obcasings.obcasingsizemodel')),
            ],
        ),
    ]