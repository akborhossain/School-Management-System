from django.contrib import admin
from .models import teacher
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display=('teacher_id','first_name','last_name','gender','date_of_birth','nid',
                  'father_name','father_nid','mother_name','mother_nid','phone_number','present_address',
                  'parmanent_address', 'image')
    
admin.site.register(teacher, TeacherAdmin)