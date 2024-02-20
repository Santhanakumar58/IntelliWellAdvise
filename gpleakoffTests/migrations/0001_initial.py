# Generated by Django 5.0.1 on 2024-02-07 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gpcasings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPLeakoffTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpfgid', models.PositiveIntegerField()),
                ('gpwellid', models.PositiveIntegerField()),
                ('gpanalyst', models.CharField(max_length=30)),
                ('gprecorded_Date', models.DateField()),
                ('gpmudWeight', models.FloatField()),
                ('gpopenholeLength', models.FloatField()),
                ('gpcasingSize', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gpcasings.gpcasingsizemodel')),
            ],
        ),
    ]
