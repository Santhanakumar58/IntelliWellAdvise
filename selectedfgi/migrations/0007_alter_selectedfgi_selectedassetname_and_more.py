# Generated by Django 4.1 on 2023-04-28 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("selectedfgi", "0006_alter_selectedfgi_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="selectedfgi",
            name="selectedassetname",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="selectedfgi",
            name="selectedblockname",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="selectedfgi",
            name="selectedfieldname",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="selectedfgi",
            name="selectedlayername",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="selectedfgi",
            name="selectedsublayername",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]