from student.models import Student
from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegistrationForm
from django import forms


def register_student(request):
    if request.method=="POST":
         form=StudentRegistrationForm(request.POST, request.FILES)
         if form.is_valid():
             form.save()
             print(f"Thank you for registering you are now a member")
         else:
             print(form.errors)
    else:
        form=StudentRegistrationForm()
    return render(request,"register_student.html",{
        "form":form
    })
def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{
        "students":students
    })
    


 