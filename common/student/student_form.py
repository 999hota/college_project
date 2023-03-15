from django import forms

from common.models import User, StudentDetails

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields= "__all__"

class StudentResgisterFrom(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = [
            'username','email','first_name', 'last_name','contact_number',


            'cv','cgpa','tenth_marks','twelveth_marks','dob','skills','coding_langs',
            'address','aadhaar'
            
        ]


    username = forms.CharField(max_length=255)
    username.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'username',"required":"required"})

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password',"required":"required"}))

    email = forms.EmailField()
    email.widget.attrs.update({'class': 'form-control','type':'email','placeholder':'email',"required":"required"})

    first_name = forms.CharField(max_length=255)
    first_name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'first_name',"required":"required"})

    last_name = forms.CharField(max_length=255)
    last_name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'last_name',"required":"required"})

    contact_number = forms.IntegerField()
    contact_number.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'contact_number',"required":"required"})


    cgpa = forms.FloatField()
    cgpa.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'cgpa(between 1 to 10)',"required":"required"})

    cv= forms.FileField(required= True)
    cv.widget.attrs.update({'class': 'form-control','type':'file',"required":"required"})

    tenth_marks = forms.IntegerField()
    tenth_marks.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'tenth_marks',"required":"required"})

    twelveth_marks = forms.IntegerField()
    twelveth_marks.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'twelveth_marks',"required":"required"})

    dob = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',  
            }
        )
    )

    skills = forms.CharField()
    skills.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'Coding, Mangement',"required":"required"})

    coding_langs = forms.CharField()
    coding_langs.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'C, C++, Python',"required":"required"})

    address = forms.CharField()
    address.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'address',"required":"required"})

    aadhaar = forms.CharField()
    aadhaar.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'aadhaar',"required":"required"})




