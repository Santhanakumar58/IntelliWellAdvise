from django.db import models
from gpdrillingsummaary.models import GPDrillingSummary


class GPDrillingOps(models.Model):  
    gpfgId = models.PositiveIntegerField()
    gpwellid = models.PositiveIntegerField() 
    gpdrillingid = models.ForeignKey(GPDrillingSummary, on_delete=models.CASCADE)
    gpops_Date = models.DateField() 
    gptime_From = models.TimeField()
    gptime_To = models.TimeField()    
    gptotalhrs = models.FloatField()
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
    gpops_Code = models.CharField(max_length = 50,choices = Operationcodes,default = 'Drilling') 
    gpops_Summary = models.TextField(max_length=2000) 
    
    def __str__(self):
        return self.gpops_Code



