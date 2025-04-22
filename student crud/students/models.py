from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
