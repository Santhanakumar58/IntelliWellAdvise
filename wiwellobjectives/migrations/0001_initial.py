# Generated by Django 5.0.1 on 2024-02-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WIWellobjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wiwellid', models.PositiveIntegerField()),
                ('wiwellname', models.CharField(max_length=50)),
                ('wifgid', models.PositiveIntegerField()),
                ('wiobjectives', models.TextField(max_length=2000)),
            ],
        ),
    ]
