from django.db import models

# Create your models here.
class WIWellcompletion(models.Model):  
    wifgid = models.PositiveIntegerField()   
    wiwellid = models.PositiveIntegerField() 
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
    wiequipment =models.CharField(max_length = 50,choices = CompletionEquipmentNames,default = 'Single') 
    wiequip_Od =models.FloatField()  
    wiequip_Id =models.FloatField()  
    wiequip_Md =models.FloatField()  
    wiequip_Tvd =models.FloatField() 
    wiequip_Angle =models.FloatField()  
    
