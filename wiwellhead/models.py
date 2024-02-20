from django.db import models

# Create your models here.
class WIWellhead(models.Model):  
    wifgid = models.PositiveIntegerField()   
    wiwellid = models.PositiveIntegerField() 
    wiwh_Make = models.CharField(max_length=50)
    wiwh_Model = models.CharField(max_length=50)
    WHTypes= (
    ("Single" , 'Single'),
    ("Dual" , 'Dual'),
    )
    wiwh_Type =models.CharField(max_length = 50,choices = WHTypes,default = 'Single')   
    SealingTypes = (
        ("Elastomer" , 'Elastomer'),
        ("Elastomer_and_Metal" , 'Elastomer_and_Metal'),
        ("Hybrid" , 'Hybrid'),
        ("Metal_to_Metal" , 'Metal_to_Metal'),        
        ("Dual_Metal_to_Metal" , 'Dual_Metal_to_Metal')
    )
    wiseal =models.CharField(max_length = 50,choices = SealingTypes,default = 'MetaltoMetal') 
    HangerTypes = (
        ("Mandrel" , 'Mandrel'),
        ("Wrap_Around" , 'Wrap_Around'),
        ("Extended_Neck" , 'Extended_Neck'),
        ("Dual_Split" , 'Dual_Split'), 
    )
    wihanger_Type =models.CharField(max_length = 50,choices = HangerTypes,default = 'Mandrel')     
    FlangeSizes = (
        ('A1', "Bottom-7 1/16-5000  & Top 7 1/16-5000"),
        ('A2',"Bottom-7 1/16-10000 /Top 7 1/16-10000") ,   
        ('A3', "Bottom-7 1/16-15000 /Top 7 1/16-15000"),
        ('B1', "Bottom-11-2000 /Top 7 1/16-2000"),
        ('B2', "Bottom-11-2000 /Top 7 1/16-3000"),
        ('C1', "Bottom-11-3000 /Top 7 1/16-3000"),        
        ('C2',  "Bottom-11-3000 /Top 7 1/16-5000"),
        ('D1',  "Bottom-11-3000 /Top 9-3000"), 
        ('D2', "Bottom-11-3000 /Top 9-5000"),
        ('E1', "Bottom-11-5000 /Top 7 1/16-5000"),
        ('E2', "Bottom-11-5000 /Top 7 1/16-10000"),
        ('E3', "Bottom-11-5000 /Top 9 -10000"),
        ('F1', "Bottom-11-10000 /Top 7 1/16-10000"),
        ('F2', "Bottom-11-10000 /Top 7 1/16-15000"),
        ('F3', "Bottom-11-10000 /Top 9-10000"),
        ('F4', "Bottom-11-10000 /Top 11-10000"),
        ("F5", "Bottom-11-10000 /Top 11-15000"),        
        ('G1', "Bottom-13 5/8-2000 /Top 7 1/16-3000"),
        ('G2', "Bottom-13 5/8-2000 /Top 9-3000"),
        ('G3', "Bottom-13 5/8-2000 /Top 11-3000"),
        ('G4', "Bottom-13 5/8-2000 /Top 11-5000"),
        ('G5', "Bottom-13 5/8-2000 /Top 13 5/8-3000"),
        ('H1', "Bottom-13 5/8-3000 /Top 7 1/16-3000"),
        ('H2', "Bottom-13 5/8-3000 /Top 7 1/16-5000"),
        ('H3', "Bottom-13 5/8-3000/Top 9-3000"),
        ('H4', "Bottom-13 5/8-3000/Top 9-5000"),
        ('H5', "Bottom-13 5/8-3000/Top 11-3000"),
        ('H6', "Bottom-13 5/8-3000/Top 11-5000"),
        ('H7', "Bottom-13 5/8-3000/Top 13 5/8-5000"),
        ('I1', "Bottom-13 5/8-5000 /Top 7 1/16-5000"),
        ('I2', "Bottom-13 5/8-5000/Top 7 1/16-10000"),
        ('I3', "Bottom-13 5/8-5000/Top 11-5000"),
        ('I4', "Bottom-13 5/8-5000/Top 11-10000"),
        ('I5', "Bottom-13 5/8-5000/Top 13 5/8-5000"),
        ('I6', "Bottom-13 5/8-5000/Top 13 5/8-10000"),
        ('J1', "Bottom-13 5/8-10000/Top 11-15000"),
        ('J2', "Bottom-13 5/8-10000/Top 13 5/8-15000"),
        ) 
    wiflange_Size=models.CharField(max_length = 50,choices = FlangeSizes, default = 'E1') 
    Connections=(
        ('Threaded','Threaded'),
        ('Welded','Welded'),
        ('Flanged', 'Flanged'),
        ('Studded', 'Studded'),
        ('Clamphub','Clamphub'),
        ('Sliplock', 'Sliplock' )
    )
    wiconnection = models.CharField(max_length = 50,choices = Connections, default = 'Threaded') 
    ValveeSizes = (
        ('A', "2 1/16"),
        ('B', "3 1/16"),
        ('C', "3 1/8"),
        ('D', "4 1/16"),
        ('E', "5 1/16")
    )    
    wivalve_Size=models.CharField(max_length = 50,choices = ValveeSizes,default = 'A') 
    TempRatings = (
        ('K', "-75-180 F"), 
        ('L', "-50-180 F"), 
        ('N', "-50-140 F"),
        ('P', "-20-180 F"), 
        ('S', "0-140 F"), 
        ('T', "0-180 F"),
        ('U', "0-250 F"),
        ('V', "35-250 F"),
        ('X', "0-350 F"), 
        ('Y', "0-650 F")
    )    
    witemperature_Rating=models.CharField(max_length = 50,choices = TempRatings,default = 'K')     
    Materials = (
        ('AA', "Carbon / Low Alloy Steel"),
        ('BB', "Carbon / Low Alloy Steel"),
        ('CC', "Stainless Steel"),
        ('DD', "Carbon / Low Alloy Steel"),
        ('EE', "Carbon / Low Alloy Steel"),
        ('FF', "Stainless Steel"), 
        ('HH', "Corrosion Resistant Alloy"),
        ('ZZ', "User Defined")     
    )    
    wimaterial=models.CharField(max_length = 50,choices = Materials,default = 'AA')     
    Services =(
        ('AA', "General Service"),
        ('BB', "General Service"), 
        ('CC', "General Service"), 
        ('DD', "Sour Service"),
        ('EE', "Sour Service"), 
        ('FF', "Sour Service"),
        ('HH', "Sour Service"), 
        ('ZZ', "Sour Service")
       )
    wiservice=models.CharField(max_length = 50,choices = Services,default = 'AA') 

    ServiceLevels = (
        ('PL1','PL1'),
        ('PL2','PL2'),
        ('PL3','PL3'),
        ('PL4','PL4'),
        )
    wiproduct_Service_Level=models.CharField(max_length = 50,choices = ServiceLevels,default = 'PL1') 


class WITree(models.Model):  
    wiwellhead = models.ForeignKey(WIWellhead, on_delete=models.CASCADE)
    wifgid = models.PositiveIntegerField()   
    wiwellid = models.PositiveIntegerField() 
    wimake = models.CharField(max_length=50)
    wimodel = models.CharField(max_length=50)
    TreeTypes= (
    ("Dry_Vertical" , 'Dry_Vertical'),
    ("Wet_Vertical" , 'Wet_Vertical'),
    ("Dry_horizontal" , 'Dry_horizontal'),
    ("Wet_Horizontal" , 'Wet_Horizontal'),
    ("HPHT" , 'HPHT'), 
    )        
    witreetype =models.CharField(max_length = 50,choices = TreeTypes,default = 'Single')  
    PressureRatings = (
        ("K2" , '2000 psi'),
        ("K3" , '3000 psi'),
        ("K5" , '5000 psi'),
        ("K10" , '10000 psi'), 
        ("K15" , '15000 psi'),
        ("K20" , '20000 psi'), 
        ("K30" , '30000 psi'), 
    )   
    wipressure_rating =models.CharField(max_length = 50,choices = PressureRatings,default = 'K5')     
    ValveeSizes = (
        ('A', "2 1/16"),
        ('B', "3 1/16"),
        ('C', "3 1/8"),
        ('D', "4 1/16"),
        ('E', "5 1/16")
    )    
    wivalve_size=models.CharField(max_length = 50,choices = ValveeSizes,default = 'A') 
    TempRatings = (
        ('K', "-75-180 F"), 
        ('L', "-50-180 F"), 
        ('N', "-50-140 F"),
        ('P', "-20-180 F"), 
        ('S', "0-140 F"), 
        ('T', "0-180 F"),
        ('U', "0-250 F"),
        ('V', "35-250 F"),
        ('X', "0-350 F"), 
        ('Y', "0-650 F")
    )    
    witemperature_Rating=models.CharField(max_length = 50,choices = TempRatings,default = 'K')     
    Materials = (
        ('AA', "Carbon / Low Alloy Steel"),
        ('BB', "Carbon / Low Alloy Steel"),
        ('CC', "Stainless Steel"),
        ('DD', "Carbon / Low Alloy Steel"),
        ('EE', "Carbon / Low Alloy Steel"),
        ('FF', "Stainless Steel"), 
        ('HH', "Corrosion Resistant Alloy"),
        ('ZZ', "User Defined")     
    )    
    wimaterialRating=models.CharField(max_length = 50,choices = Materials,default = 'AA')     
    Services =(
        ('AA', "General Service"),
        ('BB', "General Service"), 
        ('CC', "General Service"), 
        ('DD', "Sour Service"),
        ('EE', "Sour Service"), 
        ('FF', "Sour Service"),
        ('HH', "Sour Service"), 
        ('ZZ', "Sour Service")
       )
    wiservice=models.CharField(max_length = 50,choices = Services,default = 'AA') 

    ServiceLevels = (
        ('PL1','PL1'),
        ('PL2','PL2'),
        ('PL3','PL3'),
        ('PL4','PL4'),
        )
    wiproduvt_service_level=models.CharField(max_length = 50,choices = ServiceLevels,default = 'PL1') 
 
     
    
        
