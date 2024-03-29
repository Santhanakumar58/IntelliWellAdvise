# Generated by Django 5.0.1 on 2024-02-09 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WIPerforationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifgid', models.PositiveIntegerField()),
                ('wiwellid', models.PositiveIntegerField()),
                ('wiperf_Date', models.DateField()),
                ('wiperf_Top', models.FloatField()),
                ('wiperf_Bottom', models.FloatField()),
                ('wiperf_Condition', models.CharField(choices=[('Over_Balanced', 'Over_Balanced'), ('Under_balanced', 'Under_balanced')], default='Over_Balanced', max_length=50)),
                ('wiconveyance_Method', models.CharField(choices=[('Through_Casing', 'Through_Casing'), ('Through_Tubing', 'Through_Tubing'), ('TCP', 'TCP')], default='Retrievable_Hallow', max_length=50)),
                ('wiperf_Gun_Type', models.CharField(choices=[('Retrievable_Hallow', 'Retrievable_Hallow'), ('Expendable', 'Expendable'), ('Semi_Expendable', 'Semi_Expendable')], default='Retrievable_Hallow', max_length=50)),
                ('wiperf_Gun_Size', models.CharField(choices=[('2_in', '2_in'), ('2_3/4_In', '2_3/4_in'), ('3_1/8_in', '3_1/8_in'), ('3_3/8_in', '3_3/8_in')], default='2_in', max_length=50)),
                ('wiperf_Gun_Density', models.CharField(max_length=50)),
                ('wiperf_Charges', models.CharField(max_length=50)),
                ('wiremarks', models.CharField(max_length=100)),
            ],
        ),
    ]
