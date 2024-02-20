# Generated by Django 5.0.1 on 2024-02-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OBWireline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obfgid', models.PositiveIntegerField()),
                ('obwellid', models.PositiveIntegerField()),
                ('obunitname', models.CharField(max_length=50)),
                ('obstart_Date', models.DateField()),
                ('obend_Date', models.DateField()),
                ('obexpected_liquid', models.FloatField()),
                ('obexpected_WC', models.FloatField()),
                ('obexpected_GOR', models.FloatField()),
                ('obpre_wl_liquid', models.FloatField()),
                ('obpre_wl_WC', models.FloatField()),
                ('obpre_wl_GOR', models.FloatField()),
                ('obpost_wl_liquid', models.FloatField()),
                ('obpost_wl_WC', models.FloatField()),
                ('obpost_wl_GOR', models.FloatField()),
                ('objobsummary', models.TextField(max_length=1000)),
            ],
        ),
    ]
