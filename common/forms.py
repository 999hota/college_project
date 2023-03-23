from django import forms

from .models import *

class JobsForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields='__all__'
    
    title = forms.CharField(max_length=255)
    title.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'title',"required":"required"})

    package = forms.IntegerField()
    package.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'package',"required":"required"})

    company = forms.CharField(max_length=255)
    company.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'company name',"required":"required"})

    openings = forms.IntegerField()
    openings.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'package',"required":"required"})

    profile = forms.CharField(max_length=255)
    profile.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'company name',"required":"required"})

    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',  
            }
        )
    )

    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',  
            }
        )
    )

    minimum_cgpa = forms.IntegerField()
    minimum_cgpa.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'minimum_cgpa',"required":"required"})