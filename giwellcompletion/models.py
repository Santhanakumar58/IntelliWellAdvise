from django.db import models

# Create your models here.
class GIWellcompletion(models.Model):  
    gifgid = models.PositiveIntegerField()   
    giwellid = models.PositiveIntegerField() 
    CompletionEquipmentNames= (
    ("Tubing" , 'Tubing'),
    ("PupJoint" , 'PupJoint'),
    ("FlowCoupling" , 'FlowCoupling'),
    ("SSD" , 'SSD'),
    ("WEG" , 'WEG'),
    ("SCSSSV" , 'SCSSSV'),
    ("TCPGuns" , 'TCPGuns'),
    ("Packer" , 'Packer'),
    ("LandingNipple" , 'LandingNipple'),
    ("BlastJoint" , 'BlastJoint'),
    ("PerforatedPupJoint" , 'PerforatedPupJoint'),    
    ("Tubing_end" , 'Tubing_end'),
    ("PlugbackDepth" , 'PlugbackDepth'),
    ("Hold_up_Depth" , 'Hold_up_Depth'),
    )
    giequipment =models.CharField(max_length = 50,choices = CompletionEquipmentNames,default = 'Single') 
    giequip_Od =models.FloatField()  
    giequip_Id =models.FloatField()  
    giequip_Md =models.FloatField()  
    giequip_Tvd =models.FloatField() 
    giequip_Angle =models.FloatField()  
    

