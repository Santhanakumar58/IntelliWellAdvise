# Generated by Django 4.1 on 2023-05-03 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("constantcompositionexpansiondata", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ccepvtdata",
            name="y_function",
            field=models.FloatField(blank=True, null=True),
        ),
    ]