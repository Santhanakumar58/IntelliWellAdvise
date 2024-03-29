# Generated by Django 4.1.4 on 2023-02-01 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("slickline", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SlicklineOperation",
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
                ("unitname", models.CharField(max_length=50)),
                ("op_Date", models.DateField()),
                ("time_from", models.TimeField()),
                ("time_to", models.TimeField()),
                (
                    "op_code",
                    models.CharField(
                        choices=[
                            ("None", "None"),
                            ("Operating", "Operating"),
                            ("Standby", "Standby"),
                            ("Mobilization", "Mobilization"),
                            ("Demobilization", "Demobilization"),
                            ("WaitingonEquipment", "WaitingonEquipment"),
                            ("NonProductive", "NonProductive"),
                        ],
                        default="Operating",
                        max_length=50,
                    ),
                ),
                ("op_details", models.CharField(max_length=150)),
                (
                    "slickline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="slickline.slickline",
                    ),
                ),
            ],
        ),
    ]
