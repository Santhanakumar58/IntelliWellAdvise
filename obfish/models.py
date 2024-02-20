from django.db import models

class OBFishModel(models.Model):
    obwellid =models.PositiveBigIntegerField()
    obfgid = models.PositiveBigIntegerField()
    obfish_Date= models.DateTimeField()
    obfish_Top = models.FloatField()
    obfish_Bottom = models.FloatField()
    obfish_Nature = models.CharField(max_length=50, blank=True, null=True)
    obfish_Description = models.TextField(max_length=2000, blank=True, null=True)

    def __int__(self):
        return self.obwellid
