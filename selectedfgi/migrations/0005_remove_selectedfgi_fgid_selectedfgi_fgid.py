# Generated by Django 4.0.5 on 2022-06-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectedfgi', '0004_auto_20220525_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectedfgi',
            name='FGid',
        ),
        migrations.AddField(
            model_name='selectedfgi',
            name='fgid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
