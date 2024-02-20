from django.db import models
from obdrillingsummary.models import OBDrillingSummary


class OBDrillingProblems(models.Model):  
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField() 
    obdrillingid = models.ForeignKey(OBDrillingSummary, on_delete=models.CASCADE)
    obops_Date = models.DateField() 
    HoleSizes=(
        ( '26_inch', '26_inch'),
        ( '20_inch', '20_inch'),
        ( '16_inch', '16_inch'),
        ( '12_1/4_inch', '12_1/4_inch'),
        ( '8_1/2_inch', '8_1/2_inch'),
        ( '6_1/8_inch', '6_1/8_inch'),
        ( '4_1/2_inch', '4_1/2_inch'),
    )
    obhole_Size = models.CharField(max_length=50, choices=HoleSizes, default='12_1/4_inch')
    obdepth_From = models.FloatField() 
    obdepth_To = models.FloatField() 
    obdescription = models.TextField(max_length=2500)
    obpossible_reason = models.TextField(max_length=2500)


