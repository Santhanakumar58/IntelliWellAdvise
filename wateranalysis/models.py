from django.db import models
from sublayers.models import Sublayer
 

# Create your models here.
class WaterAnalysisModel(models.Model):    
    fgId = models.PositiveIntegerField()
    wellName = models.CharField(max_length=100)
    subLayer = models.ForeignKey(Sublayer, on_delete=models.CASCADE, null=True, blank=True )   
    date = models.DateField() 
    sampleId = models.PositiveIntegerField()
    SamplingPoints =(
        ('Wellhead','Wellhead'),
        ('Flowline','Flowline'),
        ('Separator','Separator')
    )
    samplepoint = models.CharField(max_length=50, choices=SamplingPoints, default="Wellhead")
    lab = models.CharField(max_length=100)
    sodium = models.FloatField(null=True)
    calcium=models.FloatField()
    magnesium = models.FloatField()
    pottasium=models.FloatField()
    ferric = models.FloatField()
    bicarbonate=models.FloatField()
    carbonate=models.FloatField()
    sulphate = models.FloatField()
    chloride=models.FloatField()
    nitrate = models.FloatField()
    tds=models.FloatField()
    temperature = models.FloatField()
    ph=models.FloatField()
    
    def __str__(self):       
        return self.wellName 
