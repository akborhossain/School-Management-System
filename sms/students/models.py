from django.contrib.auth.hashers import make_password
from django.db import models
import datetime




class student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),]
    # Using AutoField to start from '2300000001' and auto-increment
    student_id = models.AutoField(primary_key=True, unique=True, editable=False)
    username = models.CharField(max_length=10, unique=True, default="")

    password = models.CharField(max_length=128, default=make_password("1234"))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
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
            if student.objects.filter(student_id=self.student_id).exists():
                latest_student = student.objects.last()
                self.student_id = (latest_student.student_id)+1

        self.username = str(self.student_id)
        self.image = str(self.student_id) + '.jpg'
        super(student, self).save(*args, **kwargs)
class department(models.Model):

    GROUP_CHOICES = [
    ('', 'Select Department'),  # Empty choice as a placeholder
    ('General', 'General'),
    ('Science', 'Science'),
    ('Commerce', 'Commerce'),
    ('Humanity', 'Humanity'),
]
    CLASS_CHOICES = [
        (' ', 'Select Class'),
        ('Pre-One','Pre-One' ),
        ('One', 'One'),
        ('Two','Two'),
        ('Three', 'Three'),
        ('Four', 'Four'),
        ('Five','Five'),
        ('Six','Six'),
        ('Seven','Seven'),
        ('Eight','Eight'),
        ('Nine','Nine'),
        ('Ten','Ten'),
    ]
    class_id=models.CharField(max_length=10, choices=CLASS_CHOICES)
    group=models.CharField(max_length=20, choices=GROUP_CHOICES)
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)

