from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True)
    course = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name
