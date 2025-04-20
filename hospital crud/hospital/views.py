from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from hospital.models import Hospital, Doctor
from .forms import HospitalForm, DoctorForm


# Create your views here.
def home_view(request):
    template_name = 'home.html'
    return render(request, template_name)


def hospitals_view(request):
    template_name = 'hospitals.html'
    hospital_list = Hospital.objects.all()
    return render(request, template_name, {'hospital_list': hospital_list})


def hospital_detail_view(request, pk):
    template_name = 'hospital_details.html'
    hospital = Hospital.objects.get(pk=pk)
    return render(request, template_name, {'hospital': hospital})


def hospital_create_view(request):
    template_name = 'hospital_create.html'
    success_url = reverse_lazy('hospitals')

    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = HospitalForm()

    return render(request, template_name, {'form': form})


def hospital_update_view(request, pk):
    template_name = 'hospital_edit.html'
    hospital = get_object_or_404(Hospital, pk=pk)  # safer than .get()
    success_url = reverse_lazy('hospitals')

    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = HospitalForm(instance=hospital)

    return render(request, template_name, {'form': form})


def hospital_delete_view(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    success_url = reverse_lazy('hospitals')

    if request.method == 'POST':
        hospital.delete()
        return redirect(success_url)

    return render(request, 'hospital_confirm_delete.html', {'hospital': hospital})


# DOCTORS

def doctors_view(request):
    template_name = 'doctors.html'
    doctors_list = Doctor.objects.all()
    return render(request, template_name, {'doctors_list': doctors_list})


def doctor_detail_view(request, pk):
    template_name = 'doctor_detail.html'
    doctor = Doctor.objects.get(pk=pk)
    return render(request, template_name, {'doctor': doctor})


def doctor_create_view(request):
    template_name = 'doctor_create.html'
    success_url = reverse_lazy('doctors')

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = DoctorForm()

    return render(request, template_name, {'form': form})


def doctor_update_view(request, pk):
    template_name = 'doctor_update.html'
    doctor = get_object_or_404(Doctor, pk=pk)
    success_url = reverse_lazy('doctors')

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = DoctorForm(instance=doctor)

    return render(request, template_name, {'form': form})

def doctor_delete_view(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    success_url = reverse_lazy('doctors')
    if request.method == 'POST':
        doctor.delete()
        return redirect(success_url)
    return render(request, 'doctor_confirm_delete.html', {'doctor': doctor})