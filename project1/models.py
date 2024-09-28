from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name
                
    
    def obj_to_dict(self):
        data = {
            "Id":self.id,
            "name": self.name,
            "code": self.code
        }
        return data
    

class Faculty(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    
    def obj_to_dict(self):
        data = {
            "ID":self.id,
            "first_name":self.first_name,
            "last_name": self.last_name,
            "email": self.email,
           "department": {
                "id": self.department.id,
                "name": self.department.name,
                "code": self.department.code
            }
        }
        return data
    

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    batch_code = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty = models.ManyToManyField(Faculty)

    def __str__(self):
        return self.course_name
    
    def obj_to_dict(self):
        data = {
            "ID":self.id,
            "course_name":self.course_name,
            "batch_code": self.batch_code,
            "department": {
                "id": self.department.id,
                "name": self.department.name,
                "code": self.department.code
            }
        }
        return data
    


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField(null=True, blank=True)  

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    
    def obj_to_dict(self):
        data = {
            "ID":self.id,
            "first_name":self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "date_of_birth":self.date_of_birth,
            "enrollment_date":(self.enrollment_date).strftime("%Y-%b-%d %H:%M"),
            "department": {
                "id": self.department.id,
                "name": self.department.name,
                "code": self.department.code
            }


        }
        return data

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  
 
    def obj_to_dict (self):
        data = {
            "title": self.title,
            "due_date": self.due_date
           
            }

        return data
    
    

    



