from django.db import models

class GICementPlug(models.Model):    
    giwellid =models.PositiveBigIntegerField()
    gifgid = models.PositiveBigIntegerField()
    giplug_Date= models.DateField()
    giplug_Top = models.FloatField()
    giplug_Bottom = models.FloatField()    
    gicement_Density =  models.FloatField()   
    gicement_Volume = models.FloatField()      
    giplug_Description = models.TextField(max_length=2500, blank=True, null=True)


    def __int__(self):
        return self.gpwellid

class GIPumpingData(models.Model):
    gicementplug = models.ForeignKey(GICementPlug, on_delete=models.CASCADE)
    giwellid =models.PositiveBigIntegerField()
    gifgid = models.PositiveBigIntegerField()
    gipump_Time= models.TimeField()  
    Fluids = (
        ('Pre_Flush', 'Pre_Flush'),
        ('Slurry', 'Slurry'),
        ('Post_Flush', 'Post_Flush'),
        ('Water', 'Water')
    )
    gipump_Fluid = models.CharField(max_length = 20,choices = Fluids,default = 'Pre_Flush', blank=True, null=True)
    gipump_Fluid_Density = models.FloatField() 
    gipump_Pressure = models.FloatField()   
    gipump_Rate = models.FloatField()  
    

    def __int__(self):
        return self.giwellid



# Create your models here.
