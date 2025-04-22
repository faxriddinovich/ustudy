from django.urls import path
from courses.views import courses_view, course_detail_view, add_course_view, update_course_view, delete_course_view

urlpatterns = [
    path('',courses_view, name='courses'),
    path('details/<int:pk>/',course_detail_view, name='course_details'),
    path('create/',add_course_view, name='create_course'),
    path('update/<int:pk>', update_course_view, name='update_course'),
    path('delete/<int:pk>',delete_course_view,name='delete_course'),
]