from django.shortcuts import redirect, render
from selectedGasInjector.models import SelectedGasInjector
from .models import GIGradientSurvey
from .forms import GIGradientSurveyForm
# Create your views here.

def list_gigradientsurvey(request):
    selectedwell = SelectedGasInjector.objects.first()   
    gradientsurveys = GIGradientSurvey.objects.filter(giwellid =selectedwell.wellid).all()    
    return render (request, 'gigradientsurveys/gigradientsurvey.html', {'gradientsurveys': gradientsurveys })   

def create_gigradientsurvey(request):    
   gradientsurvey = GIGradientSurvey()
   selectedwell = SelectedGasInjector.objects.first()  
   gradientsurvey.gifgid = selectedwell.fgid
   gradientsurvey.giwellid = selectedwell.wellid   
   form = GIGradientSurveyForm(request.POST or None, instance=gradientsurvey)
   if request.method =="POST":        
        gradientsurvey.fgId = selectedwell.fgid
        gradientsurvey.wellid = selectedwell.wellid  
        form = GIGradientSurveyForm(request.POST, instance=gradientsurvey)  
        print(gradientsurvey.wellid)           
        if form.is_valid(): 
            gradientsurvey.fgId = selectedwell.fgid
            gradientsurvey.wellid = selectedwell.wellid        
            gradientsurvey.save()           
           
            return redirect ('gigradientsurveys:list_gigradientsurvey') 
   return render (request, 'gigradientsurveys/gigradientsurvey_form.html', {'form': form})

def update_gigradientsurvey(request, id): 
   gradientsurvey = GIGradientSurvey.objects.get(id=id)
   form = GIGradientSurveyForm(request.POST or None, instance=gradientsurvey)
   if request.method =="POST":
        form = GIGradientSurveyForm(request.POST, request.FILES, instance=gradientsurvey)
        if form.is_valid():
            form.save()            
            return redirect ('gigradientsurveys:list_gigradientsurvey')
   return render (request, 'gigradientsurveys/gigradientsurvey_form.html', {'form': form, 'gradientsurvey':gradientsurvey})

def delete_gigradientsurvey(request, id):
   gradientsurvey = GIGradientSurvey.objects.get(id=id)   
   if request.method == 'POST' :
       gradientsurvey.delete()
       return redirect ('gigradientsurveys:list_gigradientsurvey')
   return render (request, 'gigradientsurveys/gigradientsurvey_confirm_delete.html', {'gradientsurvey':gradientsurvey})


