# Generated by Django 4.1.4 on 2023-02-13 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fish", "0002_alter_fishmodel_fish_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fishmodel",
            name="fish_Description",
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
