# Generated by Django 5.0.1 on 2024-02-08 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BridgePlug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wellid', models.PositiveBigIntegerField()),
                ('fgid', models.PositiveBigIntegerField()),
                ('plug_Date', models.DateField()),
                ('plug_type', models.CharField(blank=True, choices=[('Bridge_Plug', 'Bridge_Plug'), ('Cement_Retainer', 'Cement_Retainer')], default='1', max_length=20, null=True)),
                ('plug_Depth', models.FloatField()),
                ('casing_Size', models.CharField(blank=True, choices=[('4', '4'), ('4 1/2', '4 1/2'), ('5', '5'), ('5 1/2', '5 1/2'), ('6 5/8', '6 5/8'), ('7', '7'), ('7 5/8', '7 5/8'), ('7 3/4', '7 3/4'), ('8 5/8', '8 5/8'), ('9 5/8', '9 5/8'), ('10 3/4', '10 3/3'), ('11 3/4', '11 3/3'), ('13 3/8', '13 3/8'), ('16', '16'), ('18 5/8', '18 5/8'), ('20', '20')], default='1', max_length=20, null=True)),
                ('plug_OD', models.FloatField()),
                ('setting_range_ppf', models.TextField(blank=True, max_length=25, null=True)),
                ('setting_mechanism', models.CharField(blank=True, choices=[('Mechanical', 'Mechanical'), ('Wireline', 'Wireline')], default='1', max_length=20, null=True)),
                ('plug_Make', models.TextField(blank=True, max_length=50, null=True)),
                ('plug_Model', models.TextField(blank=True, max_length=50, null=True)),
                ('Pressure_rating', models.FloatField()),
                ('Temperature_rating', models.FloatField()),
                ('plug_setting_Problems', models.TextField(blank=True, max_length=2500, null=True)),
            ],
        ),
    ]