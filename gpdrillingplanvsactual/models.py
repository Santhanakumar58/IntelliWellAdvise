from django.db import models


class GPDrillingPlanVsActual(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField() 
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
    gpsection = models.TextField(max_length=100, choices=Sections, default='26_inch') 
    gpsection_Depth_Plan = models.FloatField()
    gpplan_Days = models.FloatField()   
    gpsection_Depth_Actual = models.FloatField()
    gpactual_Days = models.FloatField() 
    gpreason_for_Deviation = models.TextField(max_length=2000) 
    
    def __int__ (self):
        return self.gpwellid

