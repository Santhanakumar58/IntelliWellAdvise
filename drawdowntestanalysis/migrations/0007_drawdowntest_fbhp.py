# Generated by Django 4.1.4 on 2023-02-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "drawdowntestanalysis",
            "0006_drawdowntest_guess_value_drawdowntest_liquid_rate",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="drawdowntest",
            name="fbhp",
            field=models.FloatField(blank=True, default=1000, null=True),
        ),
    ]
