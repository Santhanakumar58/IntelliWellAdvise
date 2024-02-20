from django.db import models
from obdrillingsummary.models import OBDrillingSummary


class OBDrillingOps(models.Model):  
    obfgId = models.PositiveIntegerField()
    obwellid = models.PositiveIntegerField() 
    obdrillingid = models.ForeignKey(OBDrillingSummary, on_delete=models.CASCADE)
    obops_Date = models.DateField() 
    obtime_From = models.TimeField()
    obtime_To = models.TimeField()    
    obtotalhrs = models.FloatField()
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
    obops_Code = models.CharField(max_length = 50,choices = Operationcodes,default = 'Drilling') 
    obops_Summary = models.TextField(max_length=2000) 
    
    def __str__(self):
        return self.obops_Code




