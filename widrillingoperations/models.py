from django.db import models
from widrillingsummary.models import WIDrillingSummary


class WIDrillingOps(models.Model):  
    wifgId = models.PositiveIntegerField()
    wiwellid = models.PositiveIntegerField() 
    widrillingid = models.ForeignKey(WIDrillingSummary, on_delete=models.CASCADE)
    wiops_Date = models.DateField() 
    witime_From = models.TimeField()
    witime_To = models.TimeField()    
    witotalhrs = models.FloatField()
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
    wiops_Code = models.CharField(max_length = 50,choices = Operationcodes,default = 'Drilling') 
    wiops_Summary = models.TextField(max_length=2000) 
    
    def __str__(self):
        return self.wiops_Code




