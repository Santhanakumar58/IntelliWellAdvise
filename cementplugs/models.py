from django.db import models

class CementPlug(models.Model):    
    wellid =models.PositiveBigIntegerField()
    fgid = models.PositiveBigIntegerField()
    plug_Date= models.DateField()
    plug_Top = models.FloatField()
    plug_Bottom = models.FloatField()    
    cement_Density =  models.FloatField()   
    cement_Volume = models.FloatField()      
    plug_Description = models.TextField(max_length=2500, blank=True, null=True)


    def __int__(self):
        return self.wellid

class PumpingData(models.Model):
    cementplug = models.ForeignKey(CementPlug, on_delete=models.CASCADE)
    wellid =models.PositiveBigIntegerField()
    fgid = models.PositiveBigIntegerField()
    pump_Time= models.TimeField()  
    Fluids = (
        ('Pre_Flush', 'Pre_Flush'),
        ('Slurry', 'Slurry'),
        ('Post_Flush', 'Post_Flush'),
        ('Water', 'Water')
    )
    pump_Fluid = models.CharField(max_length = 20,choices = Fluids,default = 'Pre_Flush', blank=True, null=True)
    pump_Fluid_Density = models.FloatField() 
    pump_Pressure = models.FloatField()   
    pump_Rate = models.FloatField()  
    

    def __int__(self):
        return self.wellid

