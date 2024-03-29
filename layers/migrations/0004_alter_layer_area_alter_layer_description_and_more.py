# Generated by Django 4.1 on 2023-04-28 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("layers", "0003_alter_layer_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="layer",
            name="area",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="layer",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="layer",
            name="layername",
            field=models.CharField(max_length=50),
        ),
    ]
