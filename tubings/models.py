from django.db import models

class TubingSizeModel(models.Model):
    tubingSize = models.CharField(max_length=10)

    def __str__(self):
        return self.tubingSize

class TubingWeightModel(models.Model):
    tubingSize = models.ForeignKey(TubingSizeModel, on_delete=models.CASCADE)
    tubingWeight = models.CharField(max_length=20)
    tubingID = models.DecimalField(max_digits=10, decimal_places=3)
   
    def __str__(self):
        return self.tubingWeight

class TubingGradeModel(models.Model):    
    tubingWeight = models.ForeignKey(TubingWeightModel, on_delete=models.CASCADE)
    tubingGrade = models.CharField(max_length=20)
    collapsePressure = models.DecimalField(decimal_places=3, max_digits=10)
    burstPressure = models.DecimalField(decimal_places=3, max_digits=10)

    def __str__(self):
        return self.tubingGrade

class TubingModel(models.Model):      
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
    Tubing_Types = (
    ("Tubing" , 'Tubing'),
    ("PupJoint" , 'PupJoint'),
    ("FlowCoupling" , 'FlowCoupling'),
    ("SSD" , 'SSD'),
    ("WEG" , 'WEG'),
    ("SCSSSV" , 'SCSSSV'),
    ("TCPGuns" , 'TCPGuns'),
    ("Packer" , 'Packer'),
    ("LandingNipple" , 'LandingNipple'),
    ("BlastJoint" , 'BlastJoint'),
    ("PerforatedPupJoint" , 'PerforatedPupJoint'),    
    ("Tubing_end" , 'Tubing_end'),
    ("PlugbackDepth" , 'PlugbackDepth'),
    ("Hold_up_Depth" , 'Hold_up_Depth'),
    )
    tubingType = models.CharField(max_length = 20,choices = Tubing_Types,default = 'Surface', blank=True, null=True)
    tubingSize=models.ForeignKey(TubingSizeModel, on_delete=models.SET_NULL, blank=True, null=True, related_name='tubingSizes')
    tubingWeight=models.ForeignKey(TubingWeightModel, on_delete=models.SET_NULL, blank=True, null=True, related_name='tubingWeights')
    tubingGrade=models.ForeignKey(TubingGradeModel, on_delete=models.SET_NULL, blank=True, null=True,related_name='tubingGrades' )
    tubingID = models.FloatField(blank=True, null=True)
    collapsePressure =models.FloatField(blank=True, null=True)
    burstPressure = models.FloatField(blank=True, null=True)
    Tubing_Threads =(        
            ("1", "STC"),
            ("2", "LTC"),  
            ("3", "BTC"), 
            ("4", "LP"), 
            ("5", "EUE"), 
            ("6", "NUE"),
            ("7", "IJ"), 
            ("8", "VAM"), 
            ("9", "NEWVAM")
        )
    threadType=models.CharField(max_length = 20,choices = Tubing_Threads,default = '1', blank=True, null=True)
    Materials =(        
            ("1", "Carbon_Steel"),
            ("2", "CRA_9Cr"),  
            ("3", "CRA_13Cr"), 
            ("4", "Inconel")            
        )
    material=models.CharField(max_length = 20,choices = Materials,default = '1', blank=True, null=True)
    depth_From=models.FloatField(blank=True, null=True)
    depth_To=models.FloatField(blank=True, null=True)
    tvd_To = models.FloatField(blank=True, null=True)
    angle_To =models.FloatField(blank=True, null=True)
    
   
    def __str__(self):
        return self.tubingType


   
    
    


