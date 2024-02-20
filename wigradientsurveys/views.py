from django.shortcuts import redirect, render
from selectedWaterInjector.models import SelectedWaterInjector
from .models import WIGradientSurvey
from .forms import WIGradientSurveyForm
# Create your views here.

def list_wigradientsurvey(request):
    selectedwell = SelectedWaterInjector.objects.first()   
    gradientsurveys = WIGradientSurvey.objects.filter(wiwellid =selectedwell.wellid).all()    
    return render (request, 'wigradientsurveys/wigradientsurvey.html', {'gradientsurveys': gradientsurveys })   

def create_wigradientsurvey(request):    
   gradientsurvey = WIGradientSurvey()
   selectedwell = SelectedWaterInjector.objects.first()  
   gradientsurvey.fgid = selectedwell.fgid
   gradientsurvey.wellid = selectedwell.wellid   
   form = WIGradientSurveyForm(request.POST or None, instance=gradientsurvey)
   if request.method =="POST":        
        gradientsurvey.fgId = selectedwell.fgid
        gradientsurvey.wellid = selectedwell.wellid  
        form = WIGradientSurveyForm(request.POST, instance=gradientsurvey)  
        print(gradientsurvey.wellid)           
        if form.is_valid(): 
            gradientsurvey.fgId = selectedwell.fgid
            gradientsurvey.wellid = selectedwell.wellid        
            gradientsurvey.save()           
           
            return redirect ('wigradientsurveys:list_wigradientsurvey') 
   return render (request, 'wigradientsurveys/wigradientsurvey_form.html', {'form': form})

def update_wigradientsurvey(request, id): 
   gradientsurvey = WIGradientSurvey.objects.get(id=id)
   form = WIGradientSurveyForm(request.POST or None, instance=gradientsurvey)
   if request.method =="POST":
        form = WIGradientSurveyForm(request.POST, request.FILES, instance=gradientsurvey)
        if form.is_valid():
            form.save()            
            return redirect ('wigradientsurveys:list_wigradientsurvey')
   return render (request, 'wigradientsurveys/wigradientsurvey_form.html', {'form': form, 'gradientsurvey':gradientsurvey})

def delete_wigradientsurvey(request, id):
   gradientsurvey = WIGradientSurvey.objects.get(id=id)   
   if request.method == 'POST' :
       gradientsurvey.delete()
       return redirect ('wigradientsurveys:list_wigradientsurvey')
   return render (request, 'wigradientsurveys/wigradientsurvey_confirm_delete.html', {'gradientsurvey':gradientsurvey})

