from django.db import models

class WICementPlug(models.Model):    
    wiwellid =models.PositiveBigIntegerField()
    wifgid = models.PositiveBigIntegerField()
    wiplug_Date= models.DateField()
    wiplug_Top = models.FloatField()
    wiplug_Bottom = models.FloatField()    
    wicement_Density =  models.FloatField()   
    wicement_Volume = models.FloatField()      
    wiplug_Description = models.TextField(max_length=2500, blank=True, null=True)


    def __int__(self):
        return self.wiwellid

class WIPumpingData(models.Model):
    wicementplug = models.ForeignKey(WICementPlug, on_delete=models.CASCADE)
    wiwellid =models.PositiveBigIntegerField()
    wifgid = models.PositiveBigIntegerField()
    wipump_Time= models.TimeField()  
    Fluids = (
        ('Pre_Flush', 'Pre_Flush'),
        ('Slurry', 'Slurry'),
        ('Post_Flush', 'Post_Flush'),
        ('Water', 'Water')
    )
    wipump_Fluid = models.CharField(max_length = 20,choices = Fluids,default = 'Pre_Flush', blank=True, null=True)
    wipump_Fluid_Density = models.FloatField() 
    wipump_Pressure = models.FloatField()   
    wipump_Rate = models.FloatField()  
    

    def __int__(self):
        return self.wiwellid



