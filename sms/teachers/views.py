from django.shortcuts import render
from django.views import View
from .forms import TeacherForm

# Create your views here.
class CreateTeacher(View):
    template_name='teachers/create.html'
    def get(self, request, *args, **kwargs):
        form=TeacherForm()
        return render(request,self.template_name,{'form':form})
    def post(self,request, *args, **kwargs):
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,self.template_name,{'success':True})
        else:
            return render(request,self.template_name,{'form':form})
