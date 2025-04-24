from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cars.forms import CarForm
from cars.models import Car


# Create your views here.
def cars_list(request):
    template_name = 'cars_list.html'
    car_list = Car.objects.all()
    return render(request, template_name, {'car_list': car_list})


def car_create(request):
    template_name = 'car_create.html'
    success_url = reverse_lazy('cars_list')

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = CarForm()
    return render(request, template_name, {'form': form})

def car_detail(request, pk):
    template_name = 'car_details.html'
    car = Car.objects.get(pk=pk)
    return render(request, template_name, {'car': car})

def car_update(request, pk):
    template_name = 'car_update.html'
    car = Car.objects.get(pk=pk)
    success_url = reverse_lazy('cars_list')
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = CarForm(instance=car)
    return render(request, template_name, {'form': form})

def car_delete(request, pk):
    template_name = 'delete_confirm.html'
    car = Car.objects.get(pk=pk)
    success_url = reverse_lazy('cars_list')
    if request.method == 'POST':
        car.delete()
        return redirect(success_url)
    return render(request, template_name, {'car': car})