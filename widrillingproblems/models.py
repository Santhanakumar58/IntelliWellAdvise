from django.db import models
from widrillingsummary.models import WIDrillingSummary


class WIDrillingProblems(models.Model):  
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField() 
    widrillingid = models.ForeignKey(WIDrillingSummary, on_delete=models.CASCADE)
    wiops_Date = models.DateField() 
    HoleSizes=(
        ( '26_inch', '26_inch'),
        ( '20_inch', '20_inch'),
        ( '16_inch', '16_inch'),
        ( '12_1/4_inch', '12_1/4_inch'),
        ( '8_1/2_inch', '8_1/2_inch'),
        ( '6_1/8_inch', '6_1/8_inch'),
        ( '4_1/2_inch', '4_1/2_inch'),
    )
    wihole_Size = models.CharField(max_length=50, choices=HoleSizes, default='12_1/4_inch')
    widepth_From = models.FloatField() 
    widepth_To = models.FloatField() 
    widescription = models.TextField(max_length=2500)
    wipossible_reason = models.TextField(max_length=2500)


