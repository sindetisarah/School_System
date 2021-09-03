from django import forms
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from django.forms import TextInput,EmailInput
from django.forms.widgets import  ClearableFileInput, DateInput, FileInput, NumberInput, Select, SelectDateWidget
from  .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        widgets = {
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

            'age':NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'age'
                }),


            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'class_name':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'ClassName'
                }),
            'students_contact':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'PhoneNumber'
                }),
            'city':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'city'
                }),
            'state':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'State'
                }),
            'parents_contact':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Parent Contact'
                }),
            
             'health_report':ClearableFileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'PhoneNumber',
                'multiple':True,
                }),
             
             'parents_name':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'ParentName'
                }),
            'academic_year':NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'academic_year'
                },
            ),
             'admission_date':DateInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'academic_year'
                },
                format='%Y-%m-%d'
                ),
            
            'nationality':Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'nationality'
                }),
            'profile_image':FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'PhoneNumber',
                'multiple':True,
                }),
            'gender':Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Gender',
                'multiple':True,
                }),
            'date_of_birth':DateInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'date_of_birth',
                
                },
                format='%Y-%m-%d'
                ),
            
        }
    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        # input_formats parses HTML5 datetime-local input to datetime field
        self.fields['academic_year'].input_formats = ('%Y-%m-%d',)
        self.fields['admission_date'].input_formats = ('%Y-%m-%d',)
        self.fields['date_of_birth'].input_formats = ('%Y-%m-%d',)


            

        