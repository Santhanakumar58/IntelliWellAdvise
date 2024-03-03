# Generated by Django 4.2.1 on 2023-12-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srpdesign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srpdesignmodel',
            name='design_Liquid',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='srpdesignmodel',
            name='plunger_Dia',
            field=models.CharField(choices=[('1.06', '1.06'), ('1.25', '1.25'), ('1.50', '1.50'), ('1.75', '1.75'), ('2.00', '2.00'), ('2.25', '2.25'), ('2.50', '2.50'), ('2.75', '2.75'), ('3.25', '3.25'), ('3.75', '3.75'), ('4.75', '4.75')], default='1.06', max_length=10),
        ),
        migrations.AlterField(
            model_name='srpdesignmodel',
            name='rod_No',
            field=models.CharField(choices=[('44', '44'), ('54', '54'), ('55', '55'), ('64', '64'), ('65', '65'), ('66', '66'), ('75', '75'), ('76', '76'), ('77', '77'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('96', '96'), ('97', '97'), ('98', '98'), ('99', '99'), ('107', '107'), ('108', '108'), ('109', '109')], default='44', max_length=100),
        ),
    ]