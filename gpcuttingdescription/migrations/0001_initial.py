# Generated by Django 5.0.1 on 2024-02-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPCuttingDescriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpfgId', models.PositiveIntegerField()),
                ('gpwellid', models.PositiveIntegerField()),
                ('gphole_Size', models.CharField(choices=[('18 1/2', '18 1/2'), ('17 1/2', '17 1/2'), ('15', '15'), ('14 3/4', '14 3/4'), ('12 1/4', '12 1/4'), ('12', '12'), ('10 5/8', '10 5/8'), ('9 7/8', '9 7/8'), ('9 5/8', '9 5/8'), ('9 1/2', '9 1/2'), ('8 3/4', '8 3/4'), ('8 5/8', '8 5/8'), ('8 1/2', '8 1/2'), ('8 3/8', '8 3/8'), ('7 7/8', '7 7/8'), ('7 5/8', '7 5/8'), ('6 3/4', '6 3/4'), ('6 5/8', '6 5/8'), ('6 1/4', '6 1/4'), ('6 1/8', '6 1/8'), ('6', '6'), ('5 7/8', '5 7/8'), ('5 5/8', '5 5/8'), ('4 3/4', '4 3/4'), ('4 5/8', '4 5/8'), ('4 1/2', '4 1/2'), ('4 1/4', '4 1/4'), ('4 1/8', '4 1/8'), ('3 7/8', '3 7/8'), ('3 3/4', '3 3/4')], default='8 1/2', max_length=20)),
                ('gptop_Depth', models.FloatField()),
                ('gpbottom_Depth', models.FloatField()),
                ('gplitho_1', models.CharField(max_length=100)),
                ('gplitho1_Composition', models.FloatField()),
                ('gplitho_2', models.CharField(max_length=100)),
                ('gplitho2_Composition', models.FloatField()),
                ('gplitho_3', models.CharField(max_length=100)),
                ('gplitho3_Composition', models.FloatField()),
                ('gpdescription', models.CharField(max_length=100)),
                ('gpremarks', models.CharField(max_length=100)),
            ],
        ),
    ]
