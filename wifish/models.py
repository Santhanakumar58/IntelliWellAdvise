from django.db import models

class WIFishModel(models.Model):
    wiwellid =models.PositiveBigIntegerField()
    wifgid = models.PositiveBigIntegerField()
    wifish_Date= models.DateTimeField()
    wifish_Top = models.FloatField()
    wifish_Bottom = models.FloatField()
    wifish_Nature = models.CharField(max_length=50, blank=True, null=True)
    wifish_Description = models.TextField(max_length=2000, blank=True, null=True)

    def __int__(self):
        return self.wiwellid