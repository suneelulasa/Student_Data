from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', student, name='Home'),
    path('create/', post_student),
    path('update/<int:id>/', put_student),
    path('delete/<int:id>/', delete_student),
]