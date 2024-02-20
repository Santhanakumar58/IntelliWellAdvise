# Generated by Django 5.0.1 on 2024-02-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OBWellcompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obfgid', models.PositiveIntegerField()),
                ('obwellid', models.PositiveIntegerField()),
                ('obequipment', models.CharField(choices=[('Tubing', 'Tubing'), ('PupJoint', 'PupJoint'), ('FlowCoupling', 'FlowCoupling'), ('SSD', 'SSD'), ('WEG', 'WEG'), ('SCSSSV', 'SCSSSV'), ('TCPGuns', 'TCPGuns'), ('Packer', 'Packer'), ('LandingNipple', 'LandingNipple'), ('BlastJoint', 'BlastJoint'), ('PerforatedPupJoint', 'PerforatedPupJoint'), ('Tubing_end', 'Tubing_end'), ('PlugbackDepth', 'PlugbackDepth'), ('Hold_up_Depth', 'Hold_up_Depth')], default='Single', max_length=50)),
                ('obequip_Od', models.FloatField()),
                ('obequip_Id', models.FloatField()),
                ('obequip_Md', models.FloatField()),
                ('obequip_Tvd', models.FloatField()),
                ('obequip_Angle', models.FloatField()),
            ],
        ),
    ]
