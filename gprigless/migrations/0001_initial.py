# Generated by Django 5.0.1 on 2024-02-18 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPRigless',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpfgid', models.PositiveIntegerField()),
                ('gpwellid', models.PositiveIntegerField()),
                ('gpunitname', models.CharField(max_length=50)),
                ('gpstart_Date', models.DateField()),
                ('gpend_Date', models.DateField()),
                ('gpexpected_liquid', models.FloatField()),
                ('gpexpected_WC', models.FloatField()),
                ('gpexpected_GOR', models.FloatField()),
                ('gppre_rigless_liquid', models.FloatField()),
                ('gppre_rigless_WC', models.FloatField()),
                ('gppre_rigless_GOR', models.FloatField()),
                ('gppost_rigless_liquid', models.FloatField()),
                ('gppost_rigless_WC', models.FloatField()),
                ('gppost_rigless_GOR', models.FloatField()),
                ('gpjobsummary', models.TextField(max_length=1000)),
            ],
        ),
    ]
