# Generated by Django 5.0.1 on 2024-02-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPPressureBuildupTestDesignModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpfgid', models.PositiveIntegerField()),
                ('gpwellid', models.PositiveIntegerField()),
                ('gpdesign_Date', models.DateField()),
                ('gpdesign_Rate', models.FloatField()),
                ('gplayer_Thickness', models.FloatField()),
                ('gplayer_Permeability', models.FloatField()),
                ('gpmu_oil', models.FloatField()),
                ('gptotal_Compressibility', models.FloatField()),
            ],
        ),
    ]