# Generated by Django 5.0.1 on 2024-02-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GIWellobjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giwellid', models.PositiveIntegerField()),
                ('giwellname', models.CharField(max_length=50)),
                ('gifgid', models.PositiveIntegerField()),
                ('giobjectives', models.TextField(max_length=2000)),
            ],
        ),
    ]
