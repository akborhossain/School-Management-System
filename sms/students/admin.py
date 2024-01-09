from django.contrib import admin

# Register your models here.
from .models import student,department
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('student_id','first_name','last_name','gender','date_of_birth','birth_number',
                  'father_name','mother_name','phone_number','present_address',
                  'parmanent_address', 'image')
    
admin.site.register(student, StudentAdmin)
class deptAdmin(admin.ModelAdmin):
    list_display=('student_id','group','class_id')
admin.site.register(department,deptAdmin)