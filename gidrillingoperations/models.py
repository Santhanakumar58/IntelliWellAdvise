from django.db import models
from gidrillingsummary.models import GIDrillingSummary


class GIDrillingOps(models.Model):  
    gifgId = models.PositiveIntegerField()
    giwellid = models.PositiveIntegerField() 
    gidrillingid = models.ForeignKey(GIDrillingSummary, on_delete=models.CASCADE)
    giops_Date = models.DateField() 
    gitime_From = models.TimeField()
    gitime_To = models.TimeField()    
    gitotalhrs = models.FloatField()
    Operationcodes = (
        ('BOPTest','BOPTest'),
        ('CasingRun','CasingRun'),
        ('Cementing','Cementing'),
        ('CementSqueeze','CementSqueeze'),
        ('Circulation','Circulation'),
        ('CoilTubing','CoilTubing'),
        ('Conditioning','Conditioning'),
        ('Coring', 'Coring'),
        ('DeviationSurvey','DeviationSurvey'),
        ('Drilling', 'Drilling'),
        ('DrillStemTest', 'DrillStemTest'),
        ('Fishing', 'Fishing'),
        ('NonProductive', 'NonProductive'),
        ('OperatingStatus', 'OperatingStatus'),
        ('Others', 'Others'),
        ('Perforating', 'Perforating'),
        ('PlugBack', 'PlugBack'),
        ('Reaming', 'Reaming'),
        ('RigDownBOP', 'RigDownBOP'),
        ('RigMove', 'RigMove'),
        ('Rigup', 'Rigup'),
        ('RigMaintenance','RigMaintenance'),
        ('RigRepair', 'RigRepair'),
        ('RigUpBOP', 'RigUpBOP'),
        ('ReplaceDrillingLine', 'ReplaceDrillingLine'),
        ('TearDown', 'TearDown'),
        ('TripIn', 'TripIn'),
        ('TripOut', 'TripOut'),
        ('WaitOnCement', 'WaitOnCement'),
        ('WaitOnWeather', 'WaitOnWeather'),
        ('WirelineLogs', 'WirelineLogs'),
        ('RunRiserEquipment','RunRiserEquipment'),
        ('RetrieveRiserEquipment', 'RetrieveRiserEquipment'),
        ('Safety','Safety'),
        ('SubSeaInstallation', 'SubSeaInstallation'),
        ('SurfaceTesting', 'SurfaceTesting'),
        ('Swabbing', 'Swabbing'),
        ('Testing', 'Testing'),
        ('Treating', 'Treating'),
        ('TubingTrip', 'TubingTrip'),
        ('WellCompletion', 'WellCompletion'),
        ('WellControl', 'WellControl')
    )
    giops_Code = models.CharField(max_length = 50,choices = Operationcodes,default = 'Drilling') 
    giops_Summary = models.TextField(max_length=2000) 
    
    def __str__(self):
        return self.giops_Code




