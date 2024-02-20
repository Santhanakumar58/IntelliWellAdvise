from django.db import models

class GIFishModel(models.Model):
    giwellid =models.PositiveBigIntegerField()
    gifgid = models.PositiveBigIntegerField()
    gifish_Date= models.DateTimeField()
    gifish_Top = models.FloatField()
    gifish_Bottom = models.FloatField()
    gifish_Nature = models.CharField(max_length=50, blank=True, null=True)
    gifish_Description = models.TextField(max_length=2000, blank=True, null=True)

    def __int__(self):
        return self.giwellid