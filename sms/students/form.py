
from django import forms
from .models import student,department
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)
DEPARTMENT_CHOICES = [
    ('', 'Select Department'),  # Empty choice as a placeholder
    ('General', 'General'),
    ('Science', 'Science'),
    ('Commerce', 'Commerce'),
    ('Humanity', 'Humanity'),
]



class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__' 
        widgets = {
            'gender': forms.ChoiceField(
                choices=student.GENDER_CHOICES,
                widget=forms.RadioSelect(attrs={'class': 'inline-radio'}),),

        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth',
            'birth_number': 'Birth Number',
            'father_name': 'Father\'s Name',
            'father_nid': 'Father\'s NID',
            'mother_name': 'Mother\'s Name',
            'mother_nid': 'Mother\'s NID',
            'phone_number': 'Phone Number',
            'present_address': 'Present Address',
            'parmanent_address': 'Permanent Address',
        }
class departmentForm(forms.ModelForm):
    class Meta:
        model=department
        fields='__all__'
        widgets = {
            'dept_name': forms.Select(
                choices=department.DEPARTMENT_CHOICES,
                widget=forms.Select()),
        }
        labels={
            'dept_name':'Group',
        }