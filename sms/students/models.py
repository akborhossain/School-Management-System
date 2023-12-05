from django.contrib.auth.hashers import make_password
from django.db import models
import datetime

class student(models.Model):
    
    # Using AutoField to start from '2300000001' and auto-increment
    student_id = models.AutoField(primary_key=True, unique=True, editable=False)
    username = models.CharField(max_length=10, unique=True, default="")

    password = models.CharField(max_length=128, default=make_password("1234"))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    date_of_birth = models.DateField()
    birth_number = models.CharField(max_length=17, unique=True)
    father_name = models.CharField(max_length=150)
    father_nid = models.IntegerField()
    mother_name = models.CharField(max_length=150)
    mother_nid = models.IntegerField()
    phone_number = models.CharField(max_length=11)
    present_address = models.CharField(max_length=500)
    parmanent_address = models.CharField(max_length=500)
    image = models.CharField(max_length=25, default="")
    
    # Use a CharField to store the last two digits of the year
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.student_id:
            # Generate student_id with the last two digits of the current year followed by eight zeroes
            current_year = str(datetime.datetime.now().year)[-2:]
            self.student_id = int(current_year + '00000001')

        self.username = str(self.student_id)
        self.image = str(self.student_id) + '.jpg'
        super(student, self).save(*args, **kwargs)
class department(models.Model):
    dept_name=models.CharField(max_length=100)
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)

