from django.contrib import admin
from .models import student_ac,teacher_ac,salary,transection,transection_detail
# Register your models here.
class StudentACAdmin(admin.ModelAdmin):
    list_display=['ac_no','payable', 'paid']
admin.site.register(student_ac, StudentACAdmin)

class TeacherACAdmin(admin.ModelAdmin):
    list_display=['ac_no','balance','paid']
admin.site.register(teacher_ac, TeacherACAdmin)

class TransectionAdmin(admin.ModelAdmin):
    list_display=['trxid','ac_no','get_way','amount','created_at','trxdid']
admin.site.register(transection, TransectionAdmin)

class TrnxDetail(admin.ModelAdmin):
    list_display=['trxdid','admission_fee','tution_fee','exam_fee','computer_lab','student_activity_fee',
                  'library_fee','development_charge','id_card','fine','total']
admin.site.register(transection_detail,TrnxDetail)

class SalaryAdmin(admin.ModelAdmin):
    list_display=['teacher_id','amount','created_at']
admin.site.register(salary, SalaryAdmin)