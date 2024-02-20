from django.db import models
from gidrillingsummary.models import GIDrillingSummary


class GIDrillingProblems(models.Model):  
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField() 
    gidrillingid = models.ForeignKey(GIDrillingSummary, on_delete=models.CASCADE)
    giops_Date = models.DateField() 
    HoleSizes=(
        ( '26_inch', '26_inch'),
        ( '20_inch', '20_inch'),
        ( '16_inch', '16_inch'),
        ( '12_1/4_inch', '12_1/4_inch'),
        ( '8_1/2_inch', '8_1/2_inch'),
        ( '6_1/8_inch', '6_1/8_inch'),
        ( '4_1/2_inch', '4_1/2_inch'),
    )
    gihole_Size = models.CharField(max_length=50, choices=HoleSizes, default='12_1/4_inch')
    gidepth_From = models.FloatField() 
    gidepth_To = models.FloatField() 
    gidescription = models.TextField(max_length=2500)
    gipossible_reason = models.TextField(max_length=2500)


