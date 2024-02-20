from django.db import models

class GPCementPlug(models.Model):    
    gpwellid =models.PositiveBigIntegerField()
    gpfgid = models.PositiveBigIntegerField()
    gpplug_Date= models.DateField()
    gpplug_Top = models.FloatField()
    gpplug_Bottom = models.FloatField()    
    gpcement_Density =  models.FloatField()   
    gpcement_Volume = models.FloatField()      
    gpplug_Description = models.TextField(max_length=2500, blank=True, null=True)


    def __int__(self):
        return self.gpwellid

class GPPumpingData(models.Model):
    gpcementplug = models.ForeignKey(GPCementPlug, on_delete=models.CASCADE)
    gpwellid =models.PositiveBigIntegerField()
    gpfgid = models.PositiveBigIntegerField()
    gppump_Time= models.TimeField()  
    Fluids = (
        ('Pre_Flush', 'Pre_Flush'),
        ('Slurry', 'Slurry'),
        ('Post_Flush', 'Post_Flush'),
        ('Water', 'Water')
    )
    gppump_Fluid = models.CharField(max_length = 20,choices = Fluids,default = 'Pre_Flush', blank=True, null=True)
    gppump_Fluid_Density = models.FloatField() 
    gppump_Pressure = models.FloatField()   
    gppump_Rate = models.FloatField()  
    

    def __int__(self):
        return self.gpwellid


