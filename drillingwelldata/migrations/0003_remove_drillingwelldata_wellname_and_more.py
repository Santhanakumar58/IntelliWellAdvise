# Generated by Django 4.1.4 on 2023-02-03 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drillingwelldata", "0002_alter_drillingwelldata_lattitude_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="drillingwelldata",
            name="wellName",
        ),
        migrations.AddField(
            model_name="drillingwelldata",
            name="wellid",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
