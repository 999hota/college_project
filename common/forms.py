from django import forms

from .models import *

class JobsForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields='__all__'