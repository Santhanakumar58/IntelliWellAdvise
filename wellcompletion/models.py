from django.db import models

# Create your models here.
class Wellcompletion(models.Model):  
    fgid = models.PositiveIntegerField()   
    wellid = models.PositiveIntegerField() 
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
    equipment =models.CharField(max_length = 50,choices = CompletionEquipmentNames,default = 'Single') 
    equip_Od =models.FloatField()  
    equip_Id =models.FloatField()  
    equip_Md =models.FloatField()  
    equip_Tvd =models.FloatField() 
    equip_Angle =models.FloatField()  
    
