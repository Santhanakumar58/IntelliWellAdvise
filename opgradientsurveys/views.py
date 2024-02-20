from django.shortcuts import redirect, render
from selectedOilProducer.models import SelectedOilProducer
from .models import GradientSurvey
from .forms import GradientSurveyForm
# Create your views here.

def list_gradientsurvey(request):
    selectedwell = SelectedOilProducer.objects.first()   
    gradientsurveys = GradientSurvey.objects.filter(wellid =selectedwell.wellid).all()    
    return render (request, 'opgradientsurveys/gradientsurvey.html', {'gradientsurveys': gradientsurveys })   

def create_gradientsurvey(request):    
   gradientsurvey = GradientSurvey()
   selectedwell = SelectedOilProducer.objects.first()  
   gradientsurvey.fgid = selectedwell.fgid
   gradientsurvey.wellid = selectedwell.wellid   
   form = GradientSurveyForm(request.POST or None, instance=gradientsurvey)
   if request.method =="POST":        
        gradientsurvey.fgId = selectedwell.fgid
        gradientsurvey.wellid = selectedwell.wellid  
        form = GradientSurveyForm(request.POST, instance=gradientsurvey)  
        print(gradientsurvey.wellid)           
        if form.is_valid(): 
            gradientsurvey.fgId = selectedwell.fgid
            gradientsurvey.wellid = selectedwell.wellid        
            gradientsurvey.save()           
           
            return redirect ('opgradientsurveys:list_gradientsurvey') 
   return render (request, 'opgradientsurveys/gradientsurvey_form.html', {'form': form})

def update_gradientsurvey(request, id): 
   gradientsurvey = GradientSurvey.objects.get(id=id)
   form = GradientSurveyForm(request.POST or None, instance=gradientsurvey)
   if request.method =="POST":
        form = GradientSurveyForm(request.POST, request.FILES, instance=gradientsurvey)
        if form.is_valid():
            form.save()            
            return redirect ('opgradientsurveys:list_gradientsurvey')
   return render (request, 'opgradientsurveys/gradientsurvey_form.html', {'form': form, 'gradientsurvey':gradientsurvey})

def delete_gradientsurvey(request, id):
   gradientsurvey = GradientSurvey.objects.get(id=id)   
   if request.method == 'POST' :
       gradientsurvey.delete()
       return redirect ('opgradientsurveys:list_gradientsurvey')
   return render (request, 'opgradientsurveys/gradientsurvey_confirm_delete.html', {'gradientsurvey':gradientsurvey})

