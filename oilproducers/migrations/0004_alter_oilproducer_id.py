# Generated by Django 4.1 on 2023-04-27 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oilproducers", "0003_auto_20220604_1112"),
    ]

    operations = [
        migrations.AlterField(
            model_name="oilproducer",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]