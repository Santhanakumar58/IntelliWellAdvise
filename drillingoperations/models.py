from django.db import models
from drillingsummary.models import DrillingSummary


class DrillingOps(models.Model):  
    fgId = models.PositiveIntegerField()
    wellid = models.PositiveIntegerField() 
    drillingid = models.ForeignKey(DrillingSummary, on_delete=models.CASCADE)
    ops_Date = models.DateField() 
    time_From = models.TimeField()
    time_To = models.TimeField()    
    totalhrs = models.FloatField()
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
    ops_Code = models.CharField(max_length = 50,choices = Operationcodes,default = 'Drilling') 
    ops_Summary = models.TextField(max_length=2000) 
    
    def __str__(self):
        return self.ops_Code


