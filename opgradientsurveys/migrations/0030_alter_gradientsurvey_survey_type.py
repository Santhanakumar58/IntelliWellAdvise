# Generated by Django 4.1.4 on 2023-01-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("opgradientsurveys", "0029_alter_gradientsurvey_survey_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gradientsurvey",
            name="survey_Type",
            field=models.CharField(
                choices=[("Static", "Static"), ("Flowing", "Flowing")],
                default="Static",
                max_length=50,
            ),
        ),
    ]
