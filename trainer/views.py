from django import forms
from trainer.models import Trainer
from trainer.forms import TrainerRegistarationForm
from django.shortcuts import render

# Create your views here.
def register_trainer(request):
    if request.method=="POST":
         form=TrainerRegistarationForm(request.POST, request.FILES)
         if form.is_valid():
             form.save()
             print(f"Thank you for registering you are now a member")
         else:
             print(form.errors)
    else:
        form=TrainerRegistarationForm()
    return render(request,"register_trainer.html",{
        "form":form
    })

def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.html",{
        "trainers":trainers

    })