from django.db import models

class GPFormatioTopsModel(models.Model):    
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField()
    Hole_Sizes=(
        ('18 1/2', '18 1/2'),
        ('17 1/2', '17 1/2'),
        ('15', '15'),
        ('14 3/4', '14 3/4'),
        ('12 1/4', '12 1/4'),
        ('12', '12'),
        ('10 5/8', '10 5/8'),
        ('9 7/8', '9 7/8'),
        ('9 5/8', '9 5/8'),
        ('9 1/2', '9 1/2'),
        ('8 3/4', '8 3/4'),
        ('8 5/8', '8 5/8'),
        ('8 1/2', '8 1/2'),
        ('8 3/8', '8 3/8'),
        ('7 7/8', '7 7/8'),
        ('7 5/8', '7 5/8'),
        ('6 3/4', '6 3/4'),        
        ('6 5/8', '6 5/8'),
        ('6 1/4', '6 1/4'),
        ('6 1/8', '6 1/8'),
        ('6', '6'),        
        ('5 7/8', '5 7/8'),
        ('5 5/8', '5 5/8'),
        ('4 3/4', '4 3/4'),
        ('4 5/8', '4 5/8'),
        ('4 1/2', '4 1/2'),
        ('4 1/4', '4 1/4'),
        ('4 1/8', '4 1/8'),
        ('3 7/8', '3 7/8'),
        ('3 3/4', '3 3/4'),
    )
    gphole_Size = models.CharField(max_length=20, choices=Hole_Sizes, default='8 1/2')    
    gpstat_Group = models.CharField(max_length=100)     
    gpstat_Formation = models.CharField(max_length=100)  
    gpstat_Member = models.CharField(max_length=100)    
    gpprognosis_Thickness = models.FloatField()   
    gpprognosis_Top = models.FloatField()    
    gpactual_Top = models.FloatField()   
    gpactual_Thickness = models.FloatField()  
    gpremarks = models.CharField(max_length=100) 
    
     
    def __int__(self):
        return self.gpwellid

