from django.db import models
from django.db.models import BigAutoField
from django.core.validators import MinValueValidator, MaxValueValidator

class Asset(models.Model):
    assetname = models.CharField(max_length=200,)
    description = models.TextField(max_length=1000)
    area = models.FloatField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    score_out_of_10= models.FloatField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])   

    def __str__(self):       
        return self.assetname
   