from django import forms
from .models import name,email
class nameForm(forms.ModelForm):
    class Meta:
        model=name
        model1=email
        fields='__all__'