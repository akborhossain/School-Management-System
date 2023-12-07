from django import forms
from .models import teacher


class TeacherForm(forms.ModelForm):

    class Meta:
        model=teacher
        exclude=['username','password','image']
        fields='__all__'