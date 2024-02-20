from django import forms
from .models import GPCasingGradeModel, GPCasingModel, GPCasingWeightModel

class GPCasingModelForm(forms.ModelForm):
    class Meta:
        model = GPCasingModel
        fields =['gpcasingType', 'gpcasingSize', 'gpcasingWeight', 'gpcasingGrade', 'gpthreadType', 'gpmaterial', 
                 'gpshoedepth', 'gpfloatCollar', 'gphangerDepth', 'gpcementTop']


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['gpcasingWeight'].queryset = GPCasingWeightModel.objects.none()
    
            if 'gpcasingSize' in self.data:
                try:
                    country_id = int(self.data.get('gpcasingSize'))
                    self.fields['gpcasingWeight'].queryset = GPCasingWeightModel.objects.filter(casingSize_id=country_id).order_by('gpcasingWeight')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                 self.fields['gpcasingWeight'].queryset = self.instance.casingSize.casingWeight_set.order_by('gpcasingWeight')
    
            self.fields['gpcasingGrade'].queryset = GPCasingGradeModel.objects.none()
            if 'gpcasingWeight' in self.data:
                try:
                    country_id = int(self.data.get('gpcasingWeight'))
                    self.fields['gpcasingGrade'].queryset = GPCasingGradeModel.objects.filter(casingWeight=country_id).order_by('gpcasingGrade')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['gpcasingGrade'].queryset = self.instance.casingGrade