from django.shortcuts import redirect, render
from selectedObserver.models import SelectedObserver
from .models import OBGradientSurvey
from .forms import OBGradientSurveyForm
# Create your views here.

def list_obgradientsurvey(request):
    selectedwell = SelectedObserver.objects.first()   
    gradientsurveys = OBGradientSurvey.objects.filter(obwellid =selectedwell.wellid).all()    
    return render (request, 'obgradientsurveys/obgradientsurvey.html', {'gradientsurveys': gradientsurveys })   

def create_obgradientsurvey(request):    
   gradientsurvey = OBGradientSurvey()
   selectedwell = SelectedObserver.objects.first()  
   gradientsurvey.fgid = selectedwell.fgid
   gradientsurvey.wellid = selectedwell.wellid   
   form = OBGradientSurveyForm(request.POST or None, instance=gradientsurvey)
   if request.method =="POST":        
        gradientsurvey.fgId = selectedwell.fgid
        gradientsurvey.wellid = selectedwell.wellid  
        form = OBGradientSurveyForm(request.POST, instance=gradientsurvey)  
        print(gradientsurvey.wellid)           
        if form.is_valid(): 
            gradientsurvey.fgId = selectedwell.fgid
            gradientsurvey.wellid = selectedwell.wellid        
            gradientsurvey.save()           
           
            return redirect ('obgradientsurveys:list_obgradientsurvey') 
   return render (request, 'obgradientsurveys/obgradientsurvey_form.html', {'form': form})

def update_obgradientsurvey(request, id): 
   gradientsurvey = OBGradientSurvey.objects.get(id=id)
   form = OBGradientSurveyForm(request.POST or None, instance=gradientsurvey)
   if request.method =="POST":
        form = OBGradientSurveyForm(request.POST, request.FILES, instance=gradientsurvey)
        if form.is_valid():
            form.save()            
            return redirect ('obgradientsurveys:list_obgradientsurvey')
   return render (request, 'obgradientsurveys/obgradientsurvey_form.html', {'form': form, 'gradientsurvey':gradientsurvey})

def delete_obgradientsurvey(request, id):
   gradientsurvey = OBGradientSurvey.objects.get(id=id)   
   if request.method == 'POST' :
       gradientsurvey.delete()
       return redirect ('obgradientsurveys:list_obgradientsurvey')
   return render (request, 'obgradientsurveys/obgradientsurvey_confirm_delete.html', {'gradientsurvey':gradientsurvey})


