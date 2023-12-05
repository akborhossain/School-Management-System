from django.db import models
from students.models import student
from teachers.models import teacher

# Create your models here.
class student_ac(models.Model):
    paid=models.FloatField()
    payable=models.FloatField()
    ac_no=models.ForeignKey(student, on_delete=models.CASCADE, unique=True, primary_key=True)

class transection_detail(models.Model):
    trxdid=models.AutoField(primary_key=True)
    admition_fee=models.FloatField()
    tution_fee=models.FloatField()
    exam_fee=models.FloatField()
    computer_lab=models.FloatField()
    student_activity_fee=models.FloatField()
    library_fee=models.FloatField()
    scout_fee=models.FloatField()
    development_charge=models.FloatField()
    id_card=models.FloatField()
    fine=models.FloatField()

class transection(models.Model):
    trxid=models.CharField(max_length=25, unique=True)
    amount=models.FloatField()
    get_way=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    ac_no=models.ForeignKey(student_ac,on_delete=models.CASCADE)
    trxdid=models.ForeignKey(transection_detail, on_delete=models.CASCADE)

class teacher_ac(models.Model):
    balance=models.FloatField()
    paid=models.FloatField()
    ac_no=models.ForeignKey(teacher, on_delete=models.CASCADE, unique=True, primary_key=True)

class salary(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    amount=models.FloatField()
    teacher_id=models.CharField(max_length=10)
