# Generated by Django 4.1 on 2023-04-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("opwellobjectivedata", "0003_opwellobjectivedata_gasrate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="opwellobjectivedata",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
