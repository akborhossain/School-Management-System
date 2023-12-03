from django.contrib.auth.hashers import make_password
from django.db import models
import datetime

class teacher(models.Model):
    
    teacher_id = models.AutoField(primary_key=True, unique=True, editable=False)
    username = models.CharField(max_length=10, unique=True, default="")

    password = models.CharField(max_length=128, default=make_password("1234"))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept=models.CharField(max_length=25)
    gender = models.CharField(max_length=6)
    date_of_birth = models.DateField()
    nid = models.CharField(max_length=17, unique=True)
    father_name = models.CharField(max_length=150)
    father_nid = models.IntegerField()
    mother_name = models.CharField(max_length=150)
    mother_nid = models.IntegerField()
    phone_number = models.CharField(max_length=11)
    present_address = models.CharField(max_length=500)
    parmanent_address = models.CharField(max_length=500)
    image = models.CharField(max_length=25 ,default="")
    
    # Use a CharField to store the last two digits of the year
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.teacher_id:
            # Generate student_id with the last two digits of the current year followed by eight zeroes
            current_year = str(datetime.datetime.now().year)[-2:]
            self.teacher_id = int(current_year + '01')

        self.username = str(self.teacher_id)
        self.image = str(self.teacher_id) + '.jpg'
        super(teacher, self).save(*args, **kwargs)
