# Generated by Django 4.0.5 on 2022-07-01 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opwellobjectivedata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opwellobjectivedata',
            name='opwellobjectiveid',
        ),
        migrations.AddField(
            model_name='opwellobjectivedata',
            name='wellid',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
