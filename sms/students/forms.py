from django import forms
from .models import student, department
import datetime

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        exclude = ['password','username', 'image']
        fields = '__all__' 
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(choices=student.GENDER_CHOICES, attrs={'type':'radio','class': 'form-check form-check-inline'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'birth_number':forms.TextInput(attrs={'class':'form-control'}),
            'father_name':forms.TextInput(attrs={'class':'form-control'}),
            'father_nid':forms.TextInput(attrs={'class':'form-control'}),
            'mother_name':forms.TextInput(attrs={'class':'form-control'}),
            'mother_nid':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'present_address': forms.Textarea(attrs={'class': 'form-control'}),
            'parmanent_address': forms.Textarea(attrs={'class': 'form-control'}),

        }
        labels  = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'gender': 'Gender',
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
        model = department
        exclude = ['student_id']
        fields = '__all__'
        widgets = {
            'group': forms.Select(choices=department.GROUP_CHOICES),
            'class_id': forms.Select(choices=department.CLASS_CHOICES),
        }
        labels = {
            'group': 'Group',
            'class_id': 'Class',
        }
