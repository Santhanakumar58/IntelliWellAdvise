# Generated by Django 4.1 on 2023-05-02 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("constantcompositionexpansion", "0002_delete_ccepvtdata"),
    ]

    operations = [
        migrations.CreateModel(
            name="CCEPVTData",
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
                ("pressure", models.FloatField()),
                ("relative_volume", models.FloatField()),
                ("y_function", models.FloatField()),
                ("density", models.FloatField()),
                (
                    "ccepvt",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="constantcompositionexpansion.ccepvt",
                    ),
                ),
            ],
        ),
    ]
