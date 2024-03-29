# Generated by Django 4.1.4 on 2023-01-30 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("coiltubing", "0003_delete_coiltubingoperation"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoiltubingOperation",
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
                ("ctname", models.CharField(max_length=50)),
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
                    "coiltubingid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="coiltubing.coiltubing",
                    ),
                ),
            ],
        ),
    ]
