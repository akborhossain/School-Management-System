from django.shortcuts import render, redirect
from django.views import View
from .forms import CreateUserForm

# Create your views here.
class LogIn(View):
    template_name=''
    def get():
        pass
    def post():
        pass

class CreateUser(View):
    template_name='home/registration.html'
    def get(self,request,*args,**kwargs):
        form=CreateUserForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request, *args, **kwargs):
        pass


