# Generated by Django 4.1.4 on 2023-02-09 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FishModel",
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
                ("wellid", models.PositiveBigIntegerField()),
                ("fgid", models.PositiveBigIntegerField()),
                ("fish_Date", models.DateTimeField()),
                ("fish_Top", models.FloatField()),
                ("fish_Bottom", models.FloatField()),
                ("fish_Nature", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "fish_Description",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
            ],
        ),
    ]