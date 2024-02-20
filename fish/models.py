from django.db import models

class FishModel(models.Model):
    wellid =models.PositiveBigIntegerField()
    fgid = models.PositiveBigIntegerField()
    fish_Date= models.DateTimeField()
    fish_Top = models.FloatField()
    fish_Bottom = models.FloatField()
    fish_Nature = models.CharField(max_length=50, blank=True, null=True)
    fish_Description = models.TextField(max_length=2000, blank=True, null=True)

    def __int__(self):
        return self.wellid