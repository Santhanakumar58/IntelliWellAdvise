from django.db import models

# Create your models here.
class GPWellcompletion(models.Model):  
    gpfgid = models.PositiveIntegerField()   
    gpwellid = models.PositiveIntegerField() 
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
    gpequipment =models.CharField(max_length = 50,choices = CompletionEquipmentNames,default = 'Single') 
    gpequip_Od =models.FloatField()  
    gpequip_Id =models.FloatField()  
    gpequip_Md =models.FloatField()  
    gpequip_Tvd =models.FloatField() 
    gpequip_Angle =models.FloatField()  
    
