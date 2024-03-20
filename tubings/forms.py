from django import forms
from .models import TubingGradeModel, TubingModel, TubingWeightModel

class TubingModelForm(forms.ModelForm):
    class Meta:
        model = TubingModel
        fields =['tubingType', 'tubingSize', 'tubingWeight', 'tubingGrade', 'threadType', 'material', 'depth_From', 'depth_To']


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['tubingWeight'].queryset = TubingWeightModel.objects.none()
    
            if 'tubingSize' in self.data:
                try:
                    country_id = int(self.data.get('tubingSize'))
                    self.fields['tubingWeight'].queryset = TubingWeightModel.objects.filter(tubingSize_id=country_id).order_by('tubingWeight')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                 self.fields['tubingWeight'].queryset = self.instance.tubingSize.tubingWeight_set.order_by('tubingWeight')
    
            self.fields['tubingGrade'].queryset = TubingGradeModel.objects.none()
            if 'tubingWeight' in self.data:
                try:
                    country_id = int(self.data.get('tubingWeight'))
                    self.fields['tubingGrade'].queryset = TubingGradeModel.objects.filter(tubingWeight=country_id).order_by('tubingGrade')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['tubingGrade'].queryset = self.instance.tubingGrade