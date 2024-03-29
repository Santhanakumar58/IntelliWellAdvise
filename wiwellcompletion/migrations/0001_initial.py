# Generated by Django 5.0.1 on 2024-02-09 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WIWellcompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifgid', models.PositiveIntegerField()),
                ('wiwellid', models.PositiveIntegerField()),
                ('wiequipment', models.CharField(choices=[('Tubing', 'Tubing'), ('PupJoint', 'PupJoint'), ('FlowCoupling', 'FlowCoupling'), ('SSD', 'SSD'), ('WEG', 'WEG'), ('SCSSSV', 'SCSSSV'), ('TCPGuns', 'TCPGuns'), ('Packer', 'Packer'), ('LandingNipple', 'LandingNipple'), ('BlastJoint', 'BlastJoint'), ('PerforatedPupJoint', 'PerforatedPupJoint'), ('Tubing_end', 'Tubing_end'), ('PlugbackDepth', 'PlugbackDepth'), ('Hold_up_Depth', 'Hold_up_Depth')], default='Single', max_length=50)),
                ('wiequip_Od', models.FloatField()),
                ('wiequip_Id', models.FloatField()),
                ('wiequip_Md', models.FloatField()),
                ('wiequip_Tvd', models.FloatField()),
                ('wiequip_Angle', models.FloatField()),
            ],
        ),
    ]
