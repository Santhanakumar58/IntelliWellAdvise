# Generated by Django 4.1.4 on 2023-02-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drawdowntestanalysis", "0004_alter_drawdowntest_file_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="drawdowntest",
            name="test_Type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Constant_Rate", "Constant_Rate"),
                    ("Constant_Pressure", "Constant_Pressure"),
                    ("Multi_Rate", "Multi_Rate"),
                ],
                default="Constant_Rate",
                max_length=50,
                null=True,
            ),
        ),
    ]
