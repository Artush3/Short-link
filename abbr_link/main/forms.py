from django import forms
from .models import Link

class CreateLink(forms.ModelForm):
    class Meta:
        model = Link 
        fields = ["link", "min_link", "author"]
        widgets = {"author": forms.HiddenInput()}
        