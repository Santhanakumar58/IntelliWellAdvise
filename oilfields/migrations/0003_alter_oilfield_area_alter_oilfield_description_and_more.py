# Generated by Django 4.1 on 2023-04-28 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oilfields", "0002_alter_oilfield_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="oilfield",
            name="area",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="oilfield",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="oilfield",
            name="oilfieldname",
            field=models.CharField(max_length=50),
        ),
    ]
