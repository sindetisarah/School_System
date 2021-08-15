from django.db import models
from django.db.models.fields.files import FileField, ImageField
from django.urls.base import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from datetime import date



class Student(models.Model):
    first_name=models.CharField(max_length=12)
    second_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    nationality_choices=(
        ('K', 'Kenya'),
        ('U', 'Uganda'),
        ('R', 'Rwanda'),
        ('S','SouthSudan')
    
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('0', 'Binary'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default="female")
    nationality=models.CharField(max_length=12,choices=nationality_choices,default="Kenya")
    class_name=models.CharField(max_length=10)
    email=models.EmailField(max_length=25)
    admission_date=models.DateField(default=date.today,null=True)
    academic_year=models.IntegerField()
    health_report=models.FileField(blank=True,upload_to='health_report/',default='default.jpg')
    profile_image=models.ImageField(upload_to='profile_pics/', default='default.jpg')
    city=models.CharField(default="City",max_length=12)
    state=models.CharField(max_length=10,blank=True,null=True)
    parents_name=models.CharField(max_length=12)
    students_contact=PhoneNumberField()
    parents_contact=PhoneNumberField()
    laptop_SerialNumber=models.CharField(max_length=12,default=True)
    
      
    
    
# class Profile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     bio=models.TextField(max_length=1000,blank=True)
#     image=models.ImageField(default='default.jpg',upload_to='profile_pics/')

#     def __str__(self):
#         return f"{self.user.username} Profile"
    
