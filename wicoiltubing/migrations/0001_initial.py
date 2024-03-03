# Generated by Django 5.0.1 on 2024-02-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WICoiltubing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifgid', models.PositiveIntegerField()),
                ('wiwellid', models.PositiveIntegerField()),
                ('wictname', models.CharField(max_length=50)),
                ('wistart_Date', models.DateField()),
                ('wiend_Date', models.DateField()),
                ('wiexpected_liquid', models.FloatField()),
                ('wiexpected_WC', models.FloatField()),
                ('wiexpected_GOR', models.FloatField()),
                ('wipre_ct_liquid', models.FloatField()),
                ('wipre_ct_WC', models.FloatField()),
                ('wipre_ct_GOR', models.FloatField()),
                ('wipost_ct_liquid', models.FloatField()),
                ('wipost_ct_WC', models.FloatField()),
                ('wipost_ct_GOR', models.FloatField()),
                ('wijobsummary', models.TextField(max_length=1000)),
            ],
        ),
    ]