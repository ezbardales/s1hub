from django import forms
from .models import Cadet

class CadetForm(forms.ModelForm):
    class Meta:
        model = Cadet
        fields = ['name', 'class_year', 'authos']