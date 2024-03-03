# Generated by Django 5.0.1 on 2024-02-19 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GIRigworkover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gifgid', models.IntegerField()),
                ('giwellid', models.IntegerField()),
                ('girigname', models.CharField(max_length=50)),
                ('gistart_Date', models.DateField()),
                ('giend_Date', models.DateField()),
                ('giexpected_liquid', models.FloatField()),
                ('giexpected_WC', models.FloatField()),
                ('giexpected_GOR', models.FloatField()),
                ('gipre_wor_liquid', models.FloatField()),
                ('gipre_wor_WC', models.FloatField()),
                ('gipre_wor_GOR', models.FloatField()),
                ('gipre_wor_Lift', models.CharField(choices=[('Self', 'Self Flow'), ('GL', 'Gas Lift'), ('ESP', 'ESP'), ('SRP', 'SRP'), ('PCP', 'PCP'), ('Jetpump', 'Jet Pump')], default='1', max_length=20)),
                ('gipost_wor_liquid', models.FloatField()),
                ('gipost_wor_WC', models.FloatField()),
                ('gipost_wor_GOR', models.FloatField()),
                ('gipost_wor_Lift', models.CharField(choices=[('Self', 'Self Flow'), ('GL', 'Gas Lift'), ('ESP', 'ESP'), ('SRP', 'SRP'), ('PCP', 'PCP'), ('Jetpump', 'Jet Pump')], default='1', max_length=20)),
                ('gijobsummary', models.TextField(max_length=1000)),
            ],
        ),
    ]