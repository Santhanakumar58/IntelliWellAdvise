# Generated by Django 5.0.1 on 2024-03-23 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multiratedrawdowntestanalysis', '0002_multiratedrawdowntest_pressure1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multiratedrawdowntest',
            old_name='file_Name',
            new_name='file_Name_csv',
        ),
        migrations.RenameField(
            model_name='multiratedrawdowntest',
            old_name='gauge_Depth',
            new_name='gauge_Depth_ft',
        ),
        migrations.RenameField(
            model_name='multiratedrawdowntest',
            old_name='initial_Res_Pres',
            new_name='initial_Res_Pres_psi',
        ),
        migrations.RenameField(
            model_name='multiratedrawdowntest',
            old_name='layer_Porosity',
            new_name='layer_Porosity_fraction',
        ),
        migrations.RenameField(
            model_name='multiratedrawdowntest',
            old_name='layer_Thickness',
            new_name='layer_Thickness_ft',
        ),
        migrations.RenameField(
            model_name='multiratedrawdowntest',
            old_name='oil_FVF',
            new_name='oil_FVF_Bo',
        ),
        migrations.RenameField(
            model_name='multiratedrawdowntest',
            old_name='oil_Viscosity',
            new_name='oil_Viscosity_cP',
        ),
        migrations.RenameField(
            model_name='multiratedrawdowntest',
            old_name='wellbore_Radius',
            new_name='wellbore_Radius_ft',
        ),
    ]
