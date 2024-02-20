from django import forms
from .models import Selectedfgi


class SelectedfgiForm(forms.ModelForm):
    class Meta:
        model = Selectedfgi
        fields =['fgid', 'selectedassetname', 'selectedblockname', 'selectedfieldname', 'selectedlayername',
                'selectedsublayername']