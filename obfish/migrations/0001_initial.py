# Generated by Django 5.0.1 on 2024-02-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OBFishModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obwellid', models.PositiveBigIntegerField()),
                ('obfgid', models.PositiveBigIntegerField()),
                ('obfish_Date', models.DateTimeField()),
                ('obfish_Top', models.FloatField()),
                ('obfish_Bottom', models.FloatField()),
                ('obfish_Nature', models.CharField(blank=True, max_length=50, null=True)),
                ('obfish_Description', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
