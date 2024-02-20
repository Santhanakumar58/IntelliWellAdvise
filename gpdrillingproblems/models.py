from django.db import models
from gpdrillingsummaary.models import GPDrillingSummary


class GPDrillingProblems(models.Model):  
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField() 
    gpdrillingid = models.ForeignKey(GPDrillingSummary, on_delete=models.CASCADE)
    gpops_Date = models.DateField() 
    HoleSizes=(
        ( '26_inch', '26_inch'),
        ( '20_inch', '20_inch'),
        ( '16_inch', '16_inch'),
        ( '12_1/4_inch', '12_1/4_inch'),
        ( '8_1/2_inch', '8_1/2_inch'),
        ( '6_1/8_inch', '6_1/8_inch'),
        ( '4_1/2_inch', '4_1/2_inch'),
    )
    gphole_Size = models.CharField(max_length=50, choices=HoleSizes, default='12_1/4_inch')
    gpdepth_From = models.FloatField() 
    gpdepth_To = models.FloatField() 
    gpdescription = models.TextField(max_length=2500)
    gppossible_reason = models.TextField(max_length=2500)

