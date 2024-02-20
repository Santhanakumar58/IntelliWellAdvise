from django import forms
from .models import OBCasingGradeModel, OBCasingModel, OBCasingWeightModel

class OBCasingModelForm(forms.ModelForm):
    class Meta:
        model = OBCasingModel
        fields =['obcasingType', 'obcasingSize', 'obcasingWeight', 'obcasingGrade', 'obthreadType', 'obmaterial', 
                 'obshoedepth', 'obfloatCollar', 'obhangerDepth', 'obcementTop']


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['obcasingWeight'].queryset = OBCasingWeightModel.objects.none()
    
            if 'obcasingSize' in self.data:
                try:
                    country_id = int(self.data.get('obcasingSize'))
                    self.fields['obcasingWeight'].queryset = OBCasingWeightModel.objects.filter(casingSize_id=country_id).order_by('obcasingWeight')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                 self.fields['obcasingWeight'].queryset = self.instance.casingSize.casingWeight_set.order_by('obcasingWeight')
    
            self.fields['obcasingGrade'].queryset = OBCasingGradeModel.objects.none()
            if 'obcasingWeight' in self.data:
                try:
                    country_id = int(self.data.get('obcasingWeight'))
                    self.fields['obcasingGrade'].queryset = OBCasingGradeModel.objects.filter(casingWeight=country_id).order_by('obcasingGrade')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['obcasingGrade'].queryset = self.instance.casingGrade