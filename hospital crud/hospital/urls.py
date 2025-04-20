from django.urls import path

from hospital.views import hospitals_view, home_view, hospital_detail_view, hospital_create_view, hospital_update_view, \
    hospital_delete_view, doctors_view, doctor_detail_view, doctor_update_view, doctor_delete_view, doctor_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('hospitals/', hospitals_view, name='hospitals'),
    path('hospitals/<int:pk>/', hospital_detail_view, name='hospital_detail'),
    path('hospitals/<int:pk>/delete/', hospital_delete_view, name='hospital_delete'),
    path('hospitals/<int:pk>/update/', hospital_update_view, name='hospital_update'),
    path('hospitals/create/', hospital_create_view, name='hospital_create'),
    path('doctors/', doctors_view, name='doctors'),
    path('doctors/<int:pk>/', doctor_detail_view, name='doctor_detail'),
    path('doctors/<int:pk>/delete/', doctor_delete_view, name='doctor_delete'),
    path('doctors/<int:pk>/update/', doctor_update_view, name='doctor_update'),
    path('doctors/create/', doctor_create_view, name='doctor_create'),
]
