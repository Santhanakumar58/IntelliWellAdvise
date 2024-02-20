from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# our new form
class ContactForm(forms.Form):
    your_contact_name = forms.CharField(required=True)
    your_email_address = forms.EmailField(required=True)
    your_organisation_ = forms.CharField(required=True)
    your_query_details = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

class SignUPForm(forms.Form):
    user_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    your_email_address = forms.EmailField(required=True)
    your_organisation_ = forms.CharField(required=True)
    your_query_details = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
