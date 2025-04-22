from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from courses.forms import CourseForm
from courses.models import Course


# Create your views here.
def courses_view(request):
    template_name = 'courses/courses.html'
    courses = Course.objects.all()
    return render(request, template_name, {'courses': courses})

def course_detail_view(request, pk):
    course = Course.objects.get(pk=pk)
    template_name = 'courses/course_details.html'
    return render(request, template_name, {'course': course})

def add_course_view(request):
    template_name = 'courses/course_create.html'
    success_url = reverse_lazy('courses')

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = CourseForm()
    return render(request, template_name, {'form': form})

def update_course_view(request, pk):
    course = Course.objects.get(pk=pk)
    template_name = 'courses/course_update.html'
    success_url = reverse_lazy('courses')
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = CourseForm(instance=course)
    return render(request, template_name, {'form': form})

def delete_course_view(request, pk):
    course = Course.objects.get(pk=pk)
    template_name = 'courses/delete_confirm.html'
    success_url = reverse_lazy('courses')
    if request.method == 'POST':
        course.delete()
        return redirect(success_url)
    return render(request, template_name, {'course': course})