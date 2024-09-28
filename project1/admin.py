from django.contrib import admin
    
from .models import Department,Faculty,Course,Student,Assignment


class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email", "enrollment_date"]

admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Student, StudentAdmin)
admin.site.register(Assignment)