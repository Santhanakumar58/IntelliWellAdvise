from django import forms
from .models import CasingGradeModel, CasingModel, CasingWeightModel

class CasingModelForm(forms.ModelForm):
    class Meta:
        model = CasingModel
        fields =['casingType', 'casingSize', 'casingWeight', 'casingGrade', 'threadType', 'material', 'shoedepth', 'floatCollar', 'hangerDepth', 'cementTop']


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['casingWeight'].queryset = CasingWeightModel.objects.none()
    
            if 'casingSize' in self.data:
                try:
                    country_id = int(self.data.get('casingSize'))
                    self.fields['casingWeight'].queryset = CasingWeightModel.objects.filter(casingSize_id=country_id).order_by('casingWeight')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                 self.fields['casingWeight'].queryset = self.instance.casingSize.casingWeight_set.order_by('casingWeight')
    
            self.fields['casingGrade'].queryset = CasingGradeModel.objects.none()
            if 'casingWeight' in self.data:
                try:
                    country_id = int(self.data.get('casingWeight'))
                    self.fields['casingGrade'].queryset = CasingGradeModel.objects.filter(casingWeight=country_id).order_by('casingGrade')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['casingGrade'].queryset = self.instance.casingGrade