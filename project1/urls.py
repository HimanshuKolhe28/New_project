from django.urls import path
from django.contrib import admin
from project1.views import create_department,get_department,update_department,create_faculty,get_faculty,update_faculty,create_course,get_course,update_course,create_student,\
get_student,update_student,delete_student,create_assignment,get_assignment,retrive_department,update_assignment

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("create_department",create_department),
    path ('get_department',get_department),
    path ('update_department/<int:pk>',update_department),
    path ('create_faculty/',create_faculty),
    path ('get_faculty/',get_faculty),
    path ('update_faculty/<int:pk>',update_faculty),
    path ('create_course',create_course),
    path ('get_course',get_course),
    path ('update_course/<int:pk>',update_course),
    path ('create_student',create_student),
    path ('get_student',get_student),
    path ('update_student/<int:pk>',update_student),
    path ('update_student/<int:pk>',update_student),
    path ('delete_student/<int:pk>',delete_student),
    path ('create_assignment',create_assignment),
    path ('get_assignment',get_assignment),
    path ('retrive_department',retrive_department),
    path ('update_assignment/<int:pk>',update_assignment)
    
]
