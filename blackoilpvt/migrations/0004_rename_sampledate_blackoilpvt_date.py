# Generated by Django 4.0.5 on 2022-06-16 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blackoilpvt', '0003_alter_blackoilpvt_sampledate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blackoilpvt',
            old_name='sampleDate',
            new_name='date',
        ),
    ]