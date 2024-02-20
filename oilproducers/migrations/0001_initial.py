# Generated by Django 3.0.14 on 2022-05-22 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oilfields', '0001_initial'),
        ('blocks', '0001_initial'),
        ('layers', '0001_initial'),
        ('assets', '0001_initial'),
        ('sublayers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OilProducer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wellname', models.CharField(max_length=50)),
                ('completiontype', models.CharField(choices=[('1', 'Single'), ('2', 'Dual'), ('3', 'Multilateral')], default='1', max_length=20)),
                ('deviationtype', models.CharField(choices=[('1', 'Vertical'), ('2', 'Deviated'), ('3', 'Horizontal')], default='1', max_length=20)),
                ('artificiallifttype', models.CharField(choices=[('1', 'Self Flow'), ('2', 'Gas Lift'), ('3', 'ESP'), ('4', 'SRP'), ('5', 'PCP'), ('6', 'Jet Pump')], default='1', max_length=20)),
                ('inflowtype', models.CharField(choices=[('1', 'Productivity Index'), ('2', 'Vogel'), ('3', 'Standings'), ('4', 'Wiggins'), ('5', 'Multirate'), ('6', 'Darcy')], default='1', max_length=20)),
                ('connectedgatheringstation', models.CharField(choices=[('1', 'GS-1'), ('2', 'GS-2'), ('3', 'GS-3'), ('4', 'GS-4'), ('5', 'GS-5'), ('6', 'GS-6')], default='1', max_length=20)),
                ('connectedheader', models.CharField(choices=[('1', 'Header-1'), ('2', 'Header-2'), ('3', 'Header-3'), ('4', 'Header-4'), ('5', 'Header-5'), ('6', 'Header-6')], default='1', max_length=20)),
                ('unitid', models.CharField(choices=[('1', 'Vertical'), ('2', 'Deviated'), ('3', 'Horizontal')], default='1', max_length=20)),
                ('is_selected', models.BooleanField()),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Asset')),
                ('block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blocks.Block')),
                ('layer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='layers.Layer')),
                ('oilfield', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='oilfields.Oilfield')),
                ('sublayer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sublayers.Sublayer')),
            ],
        ),
    ]
