# Generated by Django 4.1.4 on 2023-02-23 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("blackoilpvt", "0018_alter_blackoilpvt_pbcorrelation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Drawdowntest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fgid", models.PositiveIntegerField()),
                ("wellid", models.PositiveIntegerField()),
                ("survey_Date", models.DateField()),
                ("gauge_Depth", models.FloatField()),
                ("layer_Porosity", models.FloatField()),
                ("layer_Thickness", models.FloatField()),
                ("wellbore_Radius", models.FloatField()),
                ("total_Compressibility", models.FloatField()),
                ("initial_Res_Pres", models.FloatField()),
                ("oil_Viscosity", models.FloatField()),
                ("oil_FVF", models.FloatField()),
                (
                    "pvt_Well",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blackoilpvt.blackoilpvt",
                    ),
                ),
            ],
        ),
    ]
