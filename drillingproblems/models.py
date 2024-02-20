from django.db import models
from drillingsummary.models import DrillingSummary


class DrillingProblems(models.Model):  
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField() 
    drillingid = models.ForeignKey(DrillingSummary, on_delete=models.CASCADE)
    ops_Date = models.DateField() 
    HoleSizes=(
        ( '26_inch', '26_inch'),
        ( '20_inch', '20_inch'),
        ( '16_inch', '16_inch'),
        ( '12_1/4_inch', '12_1/4_inch'),
        ( '8_1/2_inch', '8_1/2_inch'),
        ( '6_1/8_inch', '6_1/8_inch'),
        ( '4_1/2_inch', '4_1/2_inch'),
    )
    hole_Size = models.CharField(max_length=50, choices=HoleSizes, default='12_1/4_inch')
    depth_From = models.FloatField() 
    depth_To = models.FloatField() 
    description = models.TextField(max_length=2500)
    possible_reason = models.TextField(max_length=2500)
