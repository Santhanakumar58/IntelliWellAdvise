# Generated by Django 4.2.1 on 2023-05-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wateranalysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wateranalysismodel',
            name='carbonate',
            field=models.FloatField(default=94),
            preserve_default=False,
        ),
    ]
