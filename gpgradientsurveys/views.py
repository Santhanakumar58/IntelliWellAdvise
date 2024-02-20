from django.shortcuts import redirect, render
from selectedGasProducer.models import SelectedGasProducer
from .models import GPGradientSurvey
from .forms import GPGradientSurveyForm
# Create your views here.

def list_gpgradientsurvey(request):
    selectedwell = SelectedGasProducer.objects.first()   
    gradientsurveys = GPGradientSurvey.objects.filter(gpwellid =selectedwell.wellid).all()    
    return render (request, 'gpgradientsurveys/gpgradientsurvey.html', {'gradientsurveys': gradientsurveys })   

def create_gpgradientsurvey(request):    
   gradientsurvey = GPGradientSurvey()
   selectedwell = SelectedGasProducer.objects.first()  
   gradientsurvey.fgid = selectedwell.fgid
   gradientsurvey.wellid = selectedwell.wellid   
   form = GPGradientSurveyForm(request.POST or None, instance=gradientsurvey)
   if request.method =="POST":        
        gradientsurvey.fgId = selectedwell.fgid
        gradientsurvey.wellid = selectedwell.wellid  
        form = GPGradientSurveyForm(request.POST, instance=gradientsurvey)  
        print(gradientsurvey.wellid)           
        if form.is_valid(): 
            gradientsurvey.fgId = selectedwell.fgid
            gradientsurvey.wellid = selectedwell.wellid        
            gradientsurvey.save()           
           
            return redirect ('gpgradientsurveys:list_gpgradientsurvey') 
   return render (request, 'gpgradientsurveys/gpgradientsurvey_form.html', {'form': form})

def update_gpgradientsurvey(request, id): 
   gradientsurvey = GPGradientSurvey.objects.get(id=id)
   form = GPGradientSurveyForm(request.POST or None, instance=gradientsurvey)
   if request.method =="POST":
        form =GPGradientSurveyForm(request.POST, request.FILES, instance=gradientsurvey)
        if form.is_valid():
            form.save()            
            return redirect ('gpgradientsurveys:list_gpgradientsurvey')
   return render (request, 'gpgradientsurveys/gpgradientsurvey_form.html', {'form': form, 'gradientsurvey':gradientsurvey})

def delete_gpgradientsurvey(request, id):
   gradientsurvey = GPGradientSurvey.objects.get(id=id)   
   if request.method == 'POST' :
       gradientsurvey.delete()
       return redirect ('gpgradientsurveys:list_gpgradientsurvey')
   return render (request, 'gpgradientsurveys/gpgradientsurvey_confirm_delete.html', {'gradientsurvey':gradientsurvey})


