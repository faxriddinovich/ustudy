from django.urls import path
from students.views import students_view, student_detail_view, add_student_view, update_student_view, \
    delete_student_view

urlpatterns = [
    path('',students_view, name='students'),
    path('details/<int:pk>/',student_detail_view, name='student_details'),
    path('create/',add_student_view, name='create_student'),
    path('update/<int:pk>/',update_student_view, name='update_student'),
    path('delete/<int:pk>/',delete_student_view, name='delete_student'),
]