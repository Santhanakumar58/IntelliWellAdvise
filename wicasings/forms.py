from django import forms
from .models import WICasingGradeModel, WICasingModel, WICasingWeightModel

class WICasingModelForm(forms.ModelForm):
    class Meta:
        model = WICasingModel
        fields =['wicasingType', 'wicasingSize', 'wicasingWeight', 'wicasingGrade', 'withreadType', 'wimaterial', 
                 'wishoedepth', 'wifloatCollar', 'wihangerDepth', 'wicementTop']


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['wicasingWeight'].queryset = WICasingWeightModel.objects.none()
    
            if 'wicasingSize' in self.data:
                try:
                    country_id = int(self.data.get('wicasingSize'))
                    self.fields['wicasingWeight'].queryset = WICasingWeightModel.objects.filter(casingSize_id=country_id).order_by('wicasingWeight')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                 self.fields['wicasingWeight'].queryset = self.instance.casingSize.casingWeight_set.order_by('wicasingWeight')
    
            self.fields['wicasingGrade'].queryset = WICasingGradeModel.objects.none()
            if 'wicasingWeight' in self.data:
                try:
                    country_id = int(self.data.get('wicasingWeight'))
                    self.fields['wicasingGrade'].queryset = WICasingGradeModel.objects.filter(casingWeight=country_id).order_by('wicasingGrade')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['wicasingGrade'].queryset = self.instance.casingGrade