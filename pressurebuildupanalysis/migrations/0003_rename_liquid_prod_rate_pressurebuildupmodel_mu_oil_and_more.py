# Generated by Django 4.1.4 on 2023-02-28 01:08

from django.db import migrations, models
import pressurebuildupanalysis.models


class Migration(migrations.Migration):

    dependencies = [
        ("pressurebuildupanalysis", "0002_pressurebuildupdatauploadmodel_elapsedtime"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pressurebuildupmodel",
            old_name="liquid_Prod_Rate",
            new_name="mu_oil",
        ),
        migrations.RenameField(
            model_name="pressurebuildupmodel",
            old_name="well_spacing",
            new_name="oil_FVF",
        ),
        migrations.AddField(
            model_name="pressurebuildupmodel",
            name="guess_Value",
            field=models.PositiveBigIntegerField(default=10),
        ),
        migrations.AddField(
            model_name="pressurebuildupmodel",
            name="oil_Prod_Rate",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pressurebuildupmodel",
            name="t_since_shutin",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pressurebuildupmodel",
            name="test_Type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Constant_Rate", "Constant_Rate"),
                    ("Constant_Pressure", "Constant_Pressure"),
                    ("Multi_Rate", "Multi_Rate"),
                ],
                default="Constant_Rate",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="pressurebuildupmodel",
            name="dataFile",
            field=models.FileField(
                blank=True, null=True, upload_to=pressurebuildupanalysis.models.filepath
            ),
        ),
    ]
