from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from students.forms import StudentForm
from students.models import Student


# Create your views here.
def home(request):
    return render(request, 'home.html')


def students_view(request):
    students = Student.objects.all()
    template_name = 'students/students.html'
    return render(request, template_name, {'students': students})


def student_detail_view(request, pk):
    student = Student.objects.get(pk=pk)
    template_name = 'students/student_details.html'
    return render(request, template_name, {'student': student})


def add_student_view(request):
    template_name = 'students/student_create.html'
    success_url = reverse_lazy('students')

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = StudentForm()
    return render(request, template_name,{'form':form})

def update_student_view(request, pk):
    student = Student.objects.get(pk=pk)
    template_name = 'students/student_edit.html'
    success_url = reverse_lazy('students')

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = StudentForm(instance=student)
    return render(request, template_name, {'form': form})

def delete_student_view(request, pk):
    student = Student.objects.get(pk=pk)
    template_name = 'students/delete_confirm.html'
    success_url = reverse_lazy('students')
    if request.method == 'POST':
        student.delete()
        return redirect(success_url)
    return render(request, template_name, {'student': student})