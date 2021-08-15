from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from courses.models import Course
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import CourseCreationForm
from django import forms


def course(request, event_id=None):
    instance = Course()
    if event_id:
        instance = get_object_or_404(Course, pk=event_id)
    else:
        instance = Course()

    form = CourseCreationForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
    return render(request, 'course/add_course.html', {'form': form})

def course_layout(request):
    return render(request, 'course/course.html')


