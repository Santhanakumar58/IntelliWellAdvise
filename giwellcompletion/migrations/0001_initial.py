# Generated by Django 5.0.1 on 2024-02-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GIWellcompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gifgid', models.PositiveIntegerField()),
                ('giwellid', models.PositiveIntegerField()),
                ('giequipment', models.CharField(choices=[('Tubing', 'Tubing'), ('PupJoint', 'PupJoint'), ('FlowCoupling', 'FlowCoupling'), ('SSD', 'SSD'), ('WEG', 'WEG'), ('SCSSSV', 'SCSSSV'), ('TCPGuns', 'TCPGuns'), ('Packer', 'Packer'), ('LandingNipple', 'LandingNipple'), ('BlastJoint', 'BlastJoint'), ('PerforatedPupJoint', 'PerforatedPupJoint'), ('Tubing_end', 'Tubing_end'), ('PlugbackDepth', 'PlugbackDepth'), ('Hold_up_Depth', 'Hold_up_Depth')], default='Single', max_length=50)),
                ('giequip_Od', models.FloatField()),
                ('giequip_Id', models.FloatField()),
                ('giequip_Md', models.FloatField()),
                ('giequip_Tvd', models.FloatField()),
                ('giequip_Angle', models.FloatField()),
            ],
        ),
    ]