from django.db import models


class OBDrillingPlanVsActual(models.Model):    
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField() 
    Sections=(
     ( '26_inch', '26_inch'),
     ( '23_inch', '23_inch'),
     ( '20_inch', '20_inch'),
     ( '17_1/2_inch', '17_1/2_inch'),
     ( '16_inch', '16_inch'),
     ( '12_1/4_inch', '12_1/4_inch'),
     ( '8_1/2_inch', '8_1/2_inch'),
     ( '6_1/8_inch', '6_1/8_inch'),
     ( '4_1/2_inch', '4_1/2_inch'),
     ('Completion', 'Completion'),
     ('Logging', 'Logging'),
     ('Well_Test', 'Well_Test'),
    )
    obsection = models.TextField(max_length=100, choices=Sections, default='26_inch') 
    obsection_Depth_Plan = models.FloatField()
    obplan_Days = models.FloatField()   
    obsection_Depth_Actual = models.FloatField()
    obactual_Days = models.FloatField() 
    obreason_for_Deviation = models.TextField(max_length=2000) 
    
    def __int__ (self):
        return self.obwellid


