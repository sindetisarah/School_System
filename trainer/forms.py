from django import forms
from .models import Trainer
from django.forms import TextInput,EmailInput
from django.forms.widgets import   DateInput, FileInput, NumberInput, Select

class TrainerRegistarationForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
        widgets={
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'FirstName'
                }),

            'second_name':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'SecondName'
                }),

            'gender':Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Gender',
                'multiple':True,
                }),

            'profile':FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'PhoneNumber',
                'multiple':True,
                }),

            'resume':FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'PhoneNumber',
                'multiple':True,
                }),

            'joining_date':DateInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'academic_year'
                }),
            'city':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'city'
                }),


             'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),

            'salary':NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Salary'
                }),


            'company':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Company'
                }),


            'course':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'CourseName'
                }),



        }
       