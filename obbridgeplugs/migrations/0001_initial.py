# Generated by Django 5.0.1 on 2024-02-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OBBridgePlug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obwellid', models.PositiveBigIntegerField()),
                ('obfgid', models.PositiveBigIntegerField()),
                ('obplug_Date', models.DateField()),
                ('obplug_type', models.CharField(blank=True, choices=[('Bridge_Plug', 'Bridge_Plug'), ('Cement_Retainer', 'Cement_Retainer')], default='1', max_length=20, null=True)),
                ('obplug_Depth', models.FloatField()),
                ('obcasing_Size', models.CharField(blank=True, choices=[('4', '4'), ('4 1/2', '4 1/2'), ('5', '5'), ('5 1/2', '5 1/2'), ('6 5/8', '6 5/8'), ('7', '7'), ('7 5/8', '7 5/8'), ('7 3/4', '7 3/4'), ('8 5/8', '8 5/8'), ('9 5/8', '9 5/8'), ('10 3/4', '10 3/3'), ('11 3/4', '11 3/3'), ('13 3/8', '13 3/8'), ('16', '16'), ('18 5/8', '18 5/8'), ('20', '20')], default='1', max_length=20, null=True)),
                ('obplug_OD', models.FloatField()),
                ('obsetting_range_ppf', models.TextField(blank=True, max_length=25, null=True)),
                ('obsetting_mechanism', models.CharField(blank=True, choices=[('Mechanical', 'Mechanical'), ('Wireline', 'Wireline')], default='1', max_length=20, null=True)),
                ('obplug_Make', models.TextField(blank=True, max_length=50, null=True)),
                ('obplug_Model', models.TextField(blank=True, max_length=50, null=True)),
                ('obPressure_rating', models.FloatField()),
                ('obTemperature_rating', models.FloatField()),
                ('obplug_setting_Problems', models.TextField(blank=True, max_length=2500, null=True)),
            ],
        ),
    ]