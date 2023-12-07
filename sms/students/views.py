from django.shortcuts import render, redirect
from django.views import View
from .forms import studentForm, departmentForm
from .models import student, department
from django.utils import timezone
class AdmissionView(View):
    template_name = 'students/admission.html'

    def get(self, request, *args, **kwargs):
        form = studentForm()
        form1 = departmentForm()
        return render(request, self.template_name, {'form': form, 'form1': form1})

    def post(self, request, *args, **kwargs):
        form = studentForm(request.POST)
        form1 = departmentForm(request.POST)
        
        if form.is_valid() and form1.is_valid():
            student_instance = form.save( commit=False)
            student_instance.created_at = timezone.now()  # Import timezone from django.utils
            if student_instance.save():
                print('ok')
            else:
                print('error')
            department_instance = form1.save(commit=False)
            department_instance.student_id = student_instance
            department_instance.save()
            print(student_instance)
            return redirect('admission')#, id=student_instance.student_id
        else:
            return render(request, self.template_name, {'form': form, 'form1': form1, 'success': False})

class AdmissionSuccessView(View):

    template_name = 'students/admission_success.html'

    def get(self, request, *args, **kwargs):
        student_instance = student.objects.get(student_id=kwargs['id'])
        department_instance = department.objects.get(student=student_instance)
        return render(request, self.template_name, {'student': student_instance, 'dept': department_instance, 'success': True})
