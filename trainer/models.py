from django.db import models
from django.db.models.fields.files import FileField

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=12)
    second_name=models.CharField(max_length=12)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('0', 'Binary'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default="female")
    company=models.CharField(max_length=12)
    email=models.EmailField()
    course=models.CharField(max_length=12)
    resume=FileField(upload_to='resumes/')
    city=models.CharField(max_length=10)
    profile=models.ImageField(upload_to='teachers_profile_pics/', default='default.jpg')
    joining_date=models.DateField()
    salary=models.FloatField()

