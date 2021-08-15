from django import forms
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import IntegerField
from django.forms import TextInput,EmailInput
from django.forms.widgets import  ClearableFileInput, DateInput, FileInput, NumberInput, Select, SelectDateWidget
from  .models import Course

class CourseCreationForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"
        widgets = {
            'course_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Course_name'
                }),
            'course_code':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Course_code'
                }),

            'trainer':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Trainer'
                }),


            'description':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Description'
                }),
            'course_email':EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'ClassName'
                }),
        }