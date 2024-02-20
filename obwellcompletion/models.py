from django.db import models

# Create your models here.
class OBWellcompletion(models.Model):  
    obfgid = models.PositiveIntegerField()   
    obwellid = models.PositiveIntegerField() 
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
    obequipment =models.CharField(max_length = 50,choices = CompletionEquipmentNames,default = 'Single') 
    obequip_Od =models.FloatField()  
    obequip_Id =models.FloatField()  
    obequip_Md =models.FloatField()  
    obequip_Tvd =models.FloatField() 
    obequip_Angle =models.FloatField()  
    

