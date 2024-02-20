# Generated by Django 5.0.1 on 2024-02-09 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WIFishModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wiwellid', models.PositiveBigIntegerField()),
                ('wifgid', models.PositiveBigIntegerField()),
                ('wifish_Date', models.DateTimeField()),
                ('wifish_Top', models.FloatField()),
                ('wifish_Bottom', models.FloatField()),
                ('wifish_Nature', models.CharField(blank=True, max_length=50, null=True)),
                ('wifish_Description', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
