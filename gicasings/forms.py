from django import forms
from .models import GICasingGradeModel, GICasingModel, GICasingWeightModel

class GICasingModelForm(forms.ModelForm):
    class Meta:
        model = GICasingModel
        fields =['gicasingType', 'gicasingSize', 'gicasingWeight', 'gicasingGrade', 'githreadType', 'gimaterial', 
                 'gishoedepth', 'gifloatCollar', 'gihangerDepth', 'gicementTop']


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['gicasingWeight'].queryset = GICasingWeightModel.objects.none()
    
            if 'gicasingSize' in self.data:
                try:
                    country_id = int(self.data.get('gicasingSize'))
                    self.fields['gicasingWeight'].queryset = GICasingWeightModel.objects.filter(gicasingSize_id=country_id).order_by('gicasingWeight')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                 self.fields['gicasingWeight'].queryset = self.instance.casingSize.casingWeight_set.order_by('gicasingWeight')
    
            self.fields['gicasingGrade'].queryset = GICasingGradeModel.objects.none()
            if 'gicasingWeight' in self.data:
                try:
                    country_id = int(self.data.get('gicasingWeight'))
                    self.fields['gicasingGrade'].queryset = GICasingGradeModel.objects.filter(gicasingWeight=country_id).order_by('gicasingGrade')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['gicasingGrade'].queryset = self.instance.casingGrade