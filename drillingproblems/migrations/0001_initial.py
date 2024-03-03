# Generated by Django 4.1.4 on 2023-02-15 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("drillingsummary", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DrillingProblems",
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
                ("fgId", models.PositiveIntegerField()),
                ("wellid", models.PositiveIntegerField()),
                ("ops_Date", models.DateField()),
                (
                    "hole_Size",
                    models.CharField(
                        choices=[
                            ("26_inch", "26_inch"),
                            ("20_inch", "20_inch"),
                            ("16_inch", "16_inch"),
                            ("12_1/4_inch", "12_1/4_inch"),
                            ("8_1/2_inch", "8_1/2_inch"),
                            ("6_1/8_inch", "6_1/8_inch"),
                            ("4_1/2_inch", "4_1/2_inch"),
                        ],
                        default="12_1/4_inch",
                        max_length=50,
                    ),
                ),
                ("depth_From", models.FloatField()),
                ("depth_To", models.FloatField()),
                ("description", models.TextField(max_length=2500)),
                ("possible_reason", models.TextField(max_length=2500)),
                (
                    "drillingid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="drillingsummary.drillingsummary",
                    ),
                ),
            ],
        ),
    ]