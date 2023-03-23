from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from django.contrib.auth.models import auth
from django.contrib.auth.hashers import check_password, make_password
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .student_form import SignupForm, StudentResgisterFrom

from ..models import User, StudentDetails

from django.db import transaction

class StudentResgister(View):
    template= "signup.html"
    form_class= StudentResgisterFrom

    def get(self, request):
        context={
            'form':self.form_class
        }
        return render(request, self.template, context)


    @transaction.atomic
    def post(self,request):
        
        #--------------- creating user ----------------------
        password= make_password(request.POST.get('password'))

        user_form= SignupForm(request.POST)
        if user_form.is_valid():
            user_obj= user_form.save(commit= False)
            user_obj.password= password
            user_obj.is_active= True
            user_obj.save()
        else:
            messages.error(request, user_form.errors)
            return redirect('common:student_register')

        std_form= StudentResgisterFrom(request.POST, request.FILES)
        if std_form.is_valid():
            std_obj= std_form.save(commit=False)
            std_obj.user= user_obj
            std_obj.save()
        else:
            messages.error(request, user_form.errors)
            return redirect('common:student_register')

        messages.success(request, 'Your Data is Saved')
        return redirect('common:login')
