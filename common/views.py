from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from django.contrib.auth.models import auth
from django.contrib.auth.hashers import check_password, make_password
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, Jobs, AppliedJobs
from django.contrib.auth import authenticate
from .forms import *
class Login(View):
    template = 'login.html'
    model = User
    def get(self, request):
        data = User.objects.all()
        print(data)
        return render(request, self.template)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user=User.objects.get(email=email)
        print(user)
        if user:
            auth.login(request,user)
            return redirect('common:std_dash')
        else:
            return redirect('common:login')


class StudentDashboard(View):
    template = 'studetdash.html'
    model = User
    def get(self, request):
        job_list= Jobs.objects.all().order_by('-id')
        context={
            'job_list':job_list,
        }
        return render(request, self.template, context)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=auth.authenticate(email=email, password=password)
        if user:
            auth.login(request,user)
            pass
        else:
            pass


class JobApply(View):
    template = 'studetdash.html'
    model = Jobs

    def get(self, request, job_id):
        job =self.model.objects.get(id=job_id)
        
        if AppliedJobs.objects.filter(job=job, user=request.user).exists()==False:
            AppliedJobs.objects.create(
                job = job,
                user= request.user
            )
            messages.success(request, 'Job Application is Done')
        else:
            messages.info(request, "Already Applied")
        
        return redirect('common:std_dash')

class JobDetails(View):
    template = 'job_details.html'
    model = Jobs
    form_class=JobsForm

    def get(self, request, job_id):
        job =self.model.objects.get(id=job_id)
        context={
            'form':self.form_class(instance=job)
        }
        return render(request, self.template, context)
        