
from django import forms
from .models import student,department
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)
GROUP_CHOICES = [
    ('', 'Select Department'),  # Empty choice as a placeholder
    ('General', 'General'),
    ('Science', 'Science'),
    ('Commerce', 'Commerce'),
    ('Humanity', 'Humanity'),
]
CLASS_CHOICES = [
    ('', 'Select Class'),
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
            'group': forms.Select(
                choices=department.GROUP_CHOICES,
                widget=forms.Select()),
            'class_id': forms.Select(
                choices=department.CLASS_CHOICES,
                widget=forms.Select()),
        }
        labels={
            'group':'Group',
            'class_id':'Class',
        }