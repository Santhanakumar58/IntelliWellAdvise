from django.db import models

class GPCasingSizeModel(models.Model):
    gpcasingSize = models.CharField(max_length=20)

    def __str__(self):
        return self.gpcasingSize

class GPCasingWeightModel(models.Model):
    gpcasingSize = models.ForeignKey(GPCasingSizeModel, on_delete=models.CASCADE)
    gpcasingWeight = models.CharField(max_length=20)
    gpcasingID = models.DecimalField(max_digits=10, decimal_places=3)
   
    def __str__(self):
        return self.gpcasingWeight

class GPCasingGradeModel(models.Model):    
    gpcasingWeight = models.ForeignKey(GPCasingWeightModel, on_delete=models.CASCADE)
    gpcasingGrade = models.CharField(max_length=20)
    gpcollapsePressure = models.DecimalField(decimal_places=3, max_digits=10)
    gpburstPressure = models.DecimalField(decimal_places=3, max_digits=10)

    def __str__(self):
        return self.gpcasingGrade

class GPCasingModel(models.Model):      
    gpfgid = models.PositiveIntegerField()   
    gpwellid = models.PositiveIntegerField() 
    Casing_Types = (
        ("Surface", "Surface"),
        ("Conductor", "Conductor"),
        ("Internediate_1", "Internediate1"),
        ("Intermediate_2", "Intermediate2"),
        ("Intermediate_3", "Intermediate2"),
        ("Liner_casing", "Linercasing"),
        ("Production_Casing", "ProductionCasing"),
        ("Production_Liner", "ProductionLiner")
         )
    gpcasingType = models.CharField(max_length = 20,choices = Casing_Types,default = 'Surface', blank=True, null=True)
    gpcasingSize=models.ForeignKey(GPCasingSizeModel, on_delete=models.SET_NULL, blank=True, null=True, related_name='casingSizes')
    gpcasingWeight=models.ForeignKey(GPCasingWeightModel, on_delete=models.SET_NULL, blank=True, null=True, related_name='casingWeights')
    gpcasingGrade=models.ForeignKey(GPCasingGradeModel, on_delete=models.SET_NULL, blank=True, null=True,related_name='casingGrades' )
    gpcasingID = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)
    gpcollapsePressure =models.DecimalField(decimal_places=3, max_digits=10,  blank=True, null=True)
    gpburstPressure = models.DecimalField(decimal_places=3, max_digits=10,  blank=True, null=True)
    Casing_Threads =(        
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
    gpthreadType=models.CharField(max_length = 20,choices = Casing_Threads,default = '1', blank=True, null=True)
    Materials =(        
            ("1", "Carbon_Steel"),
            ("2", "CRA_9Cr"),  
            ("3", "CRA_13Cr"), 
            ("4", "Inconel")            
        )
    gpmaterial=models.CharField(max_length = 20,choices = Materials,default = '1', blank=True, null=True)
    gpshoedepth=models.FloatField()
    gpfloatCollar=models.FloatField()
    gphangerDepth=models.FloatField()
    gpcementTop=models.FloatField()
   
    def __str__(self):
        return self.gpcasingType


    Casing_Size = (
        ("4", "4"),
        ("4 1/2", "4 1/2"),
        ("5", "5"),
        ("5 1/2", "5 1/2"),
        ("6 5/8", "6 5/8"),
        ("7", "7"),
        ("7 5/8", "7 5/8"),
        ("7 3/4", "7 3/4"),
        ("8 5/8", "8 5/8"),
        ("9 5/8", "9 5/8"),
        ("10 3/4", "10 3/3"),
        ("11 3/4", "11 3/3"),
        ("13 3/8", "13 3/8"),
        ("16", "16"),
        ("18 5/8", "18 5/8"),
        ("20", "20"),
         )    

    Casing_weights_4h =(        
            ("1", "11.6"),
            ("2", "13.5"),  
            ("3", "15.1"), 
            ("4", "16.6"), 
            ("5", "18.8"), 
            ("6", "21.6"),
            ("7", "24.6"), 
            ("8", "26.5")        
        )
    Casing_weights_5 =(        
        ("1", "13.0"),
        ("2", "15.0"),  
        ("3", "18.0"), 
        ("4", "20.3"), 
        ("5", "20.8"), 
        ("6", "23.2"),
        ("7", "24.2")                 
    )    
    Casing_weights_5h =(        
            ("1", "14.0"),
            ("2", "15.5"),  
            ("3", "17.0"), 
            ("4", "20.0"), 
            ("5", "23.0"), 
            ("6", "26.0"),
            ("7", "32.3"), 
            ("8", "36.4"),         
    )
    
    Casing_Grades =(        
            ("1", "H-40"),
            ("2", "J-55/K-55"),
            ("3", "M-65"),
            ("4", "C-75"),  
            ("5", "L-80/N-80"), 
            ("6", "C-90"), 
            ("7", "C-95/T-95/R-95"), 
            ("8", "P-110/C-110"), 
            ("9", "Q-125"), 
            ("10", "V-150")                   
        )
    
    


