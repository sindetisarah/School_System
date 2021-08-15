from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=12)
    course_code=models.CharField(max_length=12)
    trainer=models.CharField(max_length=12,blank=True)
    description=models.CharField(max_length=30)
    course_email=models.EmailField(blank=True)
    
