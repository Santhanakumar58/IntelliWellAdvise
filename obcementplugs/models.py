from django.db import models

class OBCementPlug(models.Model):    
    obwellid =models.PositiveBigIntegerField()
    obfgid = models.PositiveBigIntegerField()
    obplug_Date= models.DateField()
    obplug_Top = models.FloatField()
    obplug_Bottom = models.FloatField()    
    obcement_Density =  models.FloatField()   
    obcement_Volume = models.FloatField()      
    obplug_Description = models.TextField(max_length=2500, blank=True, null=True)


    def __int__(self):
        return self.gpwellid

class OBPumpingData(models.Model):
    obcementplug = models.ForeignKey(OBCementPlug, on_delete=models.CASCADE)
    obwellid =models.PositiveBigIntegerField()
    obfgid = models.PositiveBigIntegerField()
    obpump_Time= models.TimeField()  
    Fluids = (
        ('Pre_Flush', 'Pre_Flush'),
        ('Slurry', 'Slurry'),
        ('Post_Flush', 'Post_Flush'),
        ('Water', 'Water')
    )
    obpump_Fluid = models.CharField(max_length = 20,choices = Fluids,default = 'Pre_Flush', blank=True, null=True)
    obpump_Fluid_Density = models.FloatField() 
    obpump_Pressure = models.FloatField()   
    obpump_Rate = models.FloatField()  
    

    def __int__(self):
        return self.obwellid


