# Generated by Django 3.0.14 on 2022-06-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oilproducers', '0002_auto_20220525_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oilproducer',
            name='completiontype',
            field=models.CharField(choices=[('Single', 'Single'), ('Dual', 'Dual'), ('Multilateral', 'Multilateral')], default='1', max_length=20),
        ),
    ]
