# Generated by Django 5.0.1 on 2024-02-07 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gpcasings', '0001_initial'),
        ('gpleakoffTests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPLeakoffTestData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gptime', models.FloatField()),
                ('gpvolume', models.FloatField()),
                ('gppressure', models.FloatField()),
                ('gpcasingSize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpcasings.gpcasingsizemodel')),
                ('gpleakoffTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpleakoffTests.gpleakofftest')),
            ],
        ),
    ]