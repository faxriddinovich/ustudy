from django.urls import path
from cars.views import cars_list, car_create, car_detail, car_update, car_delete

urlpatterns = [
    path('',cars_list,name='cars_list'),
    path('create/',car_create,name='car_create'),
    path('detail/<int:pk>/',car_detail,name='car_detail'),
    path('update/<int:pk>/',car_update,name='car_update'),
    path('delete/<int:pk>/',car_delete,name='car_delete'),
]