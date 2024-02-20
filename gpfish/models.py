from django.db import models

class GPFishModel(models.Model):
    gpwellid =models.PositiveBigIntegerField()
    gpfgid = models.PositiveBigIntegerField()
    gpfish_Date= models.DateTimeField()
    gpfish_Top = models.FloatField()
    gpfish_Bottom = models.FloatField()
    gpfish_Nature = models.CharField(max_length=50, blank=True, null=True)
    gpfish_Description = models.TextField(max_length=2000, blank=True, null=True)

    def __int__(self):
        return self.gpwellid