import json
import requests
from django.shortcuts import render
import datetime

from .models import Department,Faculty,Course,Student,Assignment
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import datetime, timedelta

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# creating Department = "POST"

def create_department(request):
    if request.method == "POST":
        params = json.loads(request.body)
        instance = Department.objects.create(
            name = params.get("name"),
            code = params.get("code")
        )
        return JsonResponse({
        "data": instance.obj_to_dict()
        })
    

# Getting the information = "GET"

def get_department(request):
    if request.method == "GET":
        params = request.GET
        response = []
        name = params.get("name")
        code = params.get("code")
        queryset = Department.objects.all()

        if name:
            queryset = queryset.filter(name=name)

        if code:
            queryset = queryset.filter(code=code)

        for instance in queryset:
            response.append(instance.obj_to_dict())

    

        return JsonResponse({
            "message": "successfully GET Department",
            "data": response
        })

# Vlookup for finding name start with

def retrive_department(request):
    if request.method == "GET":
        name_starts_with = request.GET.get("name_starts_with")
        
        queryset = Department.objects.all()

        if name_starts_with:
            queryset = queryset.filter(name__startswith=name_starts_with)
        
        response = [instance.obj_to_dict() for instance in queryset]

        return JsonResponse({
            "message": "Successfully retrieved departments",
            "data": response
        })

# Update Department = "PATCH"
  
def update_department(request, pk=None):
    if request.method == "PATCH":
        print("This is api called")
        params = json.loads(request.body)

        name = params.get('name')
        code = params.get('code')

        instance = Department.objects.get(id=pk)
        instance.name = name
        instance.code = code
        instance.save()

        return JsonResponse({
            "message": "Updated department successfully",
            "data": instance.obj_to_dict()
        })
    


'''

# Update Department = "PUT"
     
def update_department(request):
    if request.method=="PATCH":
        print ("This is api called")
        params = json.loads(request.body)
        name = params.get('name')
        id = params.get('id')
        try:
            instance = Department.objects.get(id=id)
            instance.name = name
            instance.save()
            return JsonResponse({
                "message": "Updated department sucessfully using PUT",
                "data": instance.obj_to_dict()
            })
        except Department.DoesNotExist:

            return JsonResponse({
                "message": "ID is not there",
                "data": {}
            })
'''   

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_faculty(request):
    if request.method == "POST":
        params = json.loads(request.body)
        instance = Faculty.objects.create(
            first_name = params.get("first_name"),
            last_name = params.get("last_name"),
            email = params.get("email"),
            department=Department.objects.get(id=params.get('department_id'))


        )
        return JsonResponse({
        "data": instance.obj_to_dict()
        })
    
def get_faculty(request):
    if request.method == "GET":
        params = request.GET
        response = []
        first_name = params.get("first_name")
        last_name = params.get("last_name")
        queryset = Faculty.objects.all()

        if first_name:
            queryset = queryset.filter(first_name=first_name)

        if last_name:
            queryset = queryset.filter(last_name=last_name)

        for instance in queryset:
            response.append(instance.obj_to_dict())

        return JsonResponse({
            "message": "successfully GET Faculty",
            "data": response
        })
    
# Update Department
def update_faculty(request, pk=None):
    if request.method == "PATCH":
        print("This is api called")
        params = json.loads(request.body)

        first_name = params.get('first_name')
        last_name = params.get('last_name')
        email = params.get ('email')


        instance = Faculty.objects.get(id=pk)
        instance.first_name = first_name
        instance.last_name = last_name
        instance.email = email
        instance.save()

        return JsonResponse({
            "message": "Updated Faculty successfully",
            "data": instance.obj_to_dict()
        })

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create Course


def create_course(request):
    if request.method == "POST":
        params = json.loads(request.body)
        department = Department.objects.get(id=params.get('department_id'))
        faculty_emails = params.get("faculty")
        instance = Course.objects.create(
            course_name=params.get("course_name"),
            batch_code=params.get("batch_code"),
            department=department
        )
        for email in faculty_emails:
            faculty_member, _ = Faculty.objects.get_or_create(email=email)
            instance.faculty.add(faculty_member)
        return JsonResponse({
            "message": "Course created",
            "data": instance.obj_to_dict()
        })
    
def get_course(request):
    if request.method == "GET":
        params = request.GET
        response = []
        course_name = params.get("course_name")
        batch_code = params.get("batch_code")
        queryset = Course.objects.all()

        if course_name:
            queryset = queryset.filter(course_name=course_name)

        if batch_code:
            queryset = queryset.filter(last_name=batch_code)

        for instance in queryset:
            response.append(instance.obj_to_dict())

        return JsonResponse({
            "message": "successfully GET Course",
            "data": response
        })

def update_course(request, pk=None):
    if request.method == "PATCH":
        print("This is api called")
        params = json.loads(request.body)

        course_name = params.get('course_name')
        batch_code = params.get('batch_code')


        instance = Course.objects.get(id=pk)
        instance.course_name = course_name
        instance.batch_code = batch_code
        instance.save()

        return JsonResponse({
            "message": "Updated Course successfully",
            "data": instance.obj_to_dict()
        })

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# create Query

def create_student(request):
    if request.method == "POST":
        params = json.loads(request.body)
        instance = Student.objects.create(
            first_name = params.get("first_name"),
            last_name = params.get("last_name"),
            email = params.get("email"),
            date_of_birth = params.get("date_of_birth"),
            enrollment_date =params.get("enrollment_date"),
        
            department=Department.objects.get(id=params.get('department_id'))
        )
        return JsonResponse({
        "data": instance.obj_to_dict()
        })

# get Query
'''     
def get_student(request):
    if request.method == "GET":
        params = request.GET
        response = []
        first_name = params.get("first_name")
        last_name = params.get("last_name")
        email = params.get("email")
        enrollment_date = params.get("enrollment_date")
        queryset = Student.objects.all()

        if first_name:
            queryset = queryset.filter(first_name=first_name)

        if last_name:
            queryset = queryset.filter(last_name=last_name)
        
        if email:
            queryset = queryset.filter(email=email)
       
        if enrollment_date:
            queryset = queryset.filter(enrollment_date=enrollment_date)
        

        for instance in queryset:
            response.append(instance.obj_to_dict())

        return JsonResponse({
            "message": "successfully GET Student",
            "data": response
        })
   
def get_student(request):
    if request.method == "GET":
        params = request.GET
        queryset = Student.objects.all()
        filters = {}

        for x in ["first_name", "last_name", "email", "enrollment_date"]:
            value = params.get(x)
            if value:
                filters[x] = value

        queryset = queryset.filter(**filters)

        response = [instance.obj_to_dict() for instance in queryset]

        return JsonResponse({
            "message": "successfully GET Student",
            "data": response
        })
'''   


def get_student(request):
    if request.method == "GET":
        params = request.GET
        kwargs = {}

        if 'student_name_contains' in params:
            kwargs['first_name__icontains'] = params['student_name_contains']
        
        if "date_of_birth_contains" in params:
            kwargs['date_of_birth__icontains'] = params['date_of_birth_contains']

        if 'first_name' in params and 'student_name_contains' not in params:
            kwargs['first_name'] = params['first_name']
        
        if 'last_name' in params:
            kwargs['last_name'] = params['last_name']

        if 'email' in params:
            kwargs['email'] = params['email']

        if 'date_of_birth' in params and 'date_of_birth_contains' not in params:
            kwargs['date_of_birth'] = params['date_of_birth']
        
        if 'date_of_birth_gt' in params:
            kwargs['date_of_birth__gt'] = params['date_of_birth_gt']

        if 'date_of_birth_lt' in params:
            kwargs['date_of_birth__lt'] = params['date_of_birth_lt']

        if 'enrollment_date' in params:
            kwargs['enrollment_date'] = params['enrollment_date']

        queryset = Student.objects.filter(**kwargs)

        response = [instance.obj_to_dict() for instance in queryset]
       
        if not queryset.exists():
            return JsonResponse({
                "message": "No data found",
                "data": []
            })
        

        return JsonResponse({
            "message": "Successfully GET Student",
            "data": response
        })



# Update Query
def update_student(request, pk=None):
    if request.method == "PATCH":
        print("This is api called")
        params = json.loads(request.body)

        first_name = params.get('first_name')
        last_name = params.get('last_name')
        email = params.get ("email") 
        enrollment_date = params.get ("enrollment_date")

        instance = Student.objects.get(id=pk)
        instance.first_name = first_name
        instance.last_name = last_name
        instance.email = email
        instance.enrollment_date = enrollment_date


        instance.save()

        return JsonResponse({
            "message": "Updated department successfully",
            "data": instance.obj_to_dict()
        })

# delete Query

def delete_student(request, pk=None):
    if request.method == "DELETE":
        student = Student.objects.filter(id=pk).first()
        if student:
            student_data = student.obj_to_dict()
            student.delete()
            return JsonResponse({
                "message": "Student deleted successfully",
                "data": student_data
            })

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Create Query

def create_assignment (request):
    if request.method == "POST":
        params = json.loads(request.body)
        instance = Assignment.objects.create(
            title = params.get("title"),
            due_date = params.get("due_date"),
            course=Course.objects.get(id=params.get('course_id'))
            
        )
        return JsonResponse({
        "data": instance.obj_to_dict()
        })
    
# Get Query

def get_assignment (request):
    if request.method == "GET":
        params = request.GET
        response = []
        title = params.get("title")
        due_date = params.get("due_date")
        queryset = Assignment.objects.all()

        if title:
            queryset = queryset.filter(title=title)

        if due_date:
            queryset = queryset.filter(due_date=due_date)


        for instance in queryset:
            response.append(instance.obj_to_dict())

        return JsonResponse({
            "message": "successfully GET Course",
            "data": response
        })
    

 # Update Query

def update_assignment (request,pk=None):
    if request.method == "PATCH":
        print("This is api called")
        params = json.loads(request.body)

        title = params.get('title')
        due_date = params.get('due_date')

        instance = Course.objects.get(id=pk)
        instance.title = title
        instance.due_date = due_date
        instance.save()

        return JsonResponse({
            "message": "Updated Course successfully",
            "data": instance.obj_to_dict()
        })

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
