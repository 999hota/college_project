from django.shortcuts import render, redirect, reverse
from django.utils.http import urlencode
from django.views import View

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import logout      
from .models import User, Jobs, AppliedJobs
from django.contrib.auth import authenticate
from .forms import *
from helpers import utils

def login_validate(**kwargs):
    
    if 'username' in kwargs:
        try:
            user = User.objects.get(username= kwargs['username'])
        except:
            return None
        
        if user.check_password(kwargs['password']):
            return user
        else:
            return None
    
    elif 'email' in kwargs:
        try:
            user = User.objects.get(email= kwargs['email'])
        except:
            return None
        
        if user.check_password(kwargs['password']):
            return user
        else:
            return None
    
    else:
        return None
        
class Login(View):
    template = 'login.html'
    model = User
    def get(self, request):
        return render(request, self.template)



    def send_otp(self, email, otp):
        subject = 'welcome to CMS'
        message = f'Hi {email}, welcome back. Please use this otp : {otp} for login...'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = login_validate(email=email, password=password)
        if user:
            if user.is_superuser:
                return redirect('common:admin_dash')
            # ---------------------
            otp = utils.unique_number(4)
            user.otp = otp
            user.save()
            self.send_otp(email, otp)
            # ---------------------
            return redirect(
                reverse("common:otp_verification")+'?'+urlencode({"email":email})
            )
        else:
            messages.error(request, 'Login Failed')
            return redirect('common:login')

class OtpVerification(View):
    model = User
    template = "otp.html"
    def get(self, request):
        email= request.GET.get("email")
        context = {
            "email":email
        }
        messages.info(request, f"A 4-digit otp has been sent to {email}.")
        return render(request, self.template, context)
        
    def post(self, request):
        email = request.POST.get("email")
        otp= request.POST.get("otp")

        try:
            user = self.model.objects.get(email=email, otp = otp)
            login(request, user)
            if not user.is_staff==True:
                return redirect('common:std_dash')
            else:
                return redirect('common:admin_dash')
        except:
            messages.error(request, "Otp verification failed....")
            return redirect(
                reverse("common:otp_verification")+'?'+urlencode({"email":email})
            )


class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logout successfully.....")
        return redirect("common:login")
        


class StudentDashboard(View):
    template = 'studetdash.html'
    model = User
    def get(self, request):
        job_list= Jobs.objects.all().order_by('-id')
        context={
            'job_list':job_list,
        }
        return render(request, self.template, context)



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

class AdminDashboard(View):
    template= 'admin/admin_dashboard.html'
    form = JobsForm
    model= Jobs

    def get(self, request):

        job_list= Jobs.objects.all().order_by('id')
        context= {
            'job_list':job_list,
            'form':self.form
        }
        return render(request, self.template, context)

class CreateJob(View):
    model= Jobs
    form_class= JobsForm
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New job is addded.....')
        else:
            messages.error(request, form.errors)

        return redirect('common:admin_dash')



from .models import STATUS_S
class GetAppliedStudentList(View):
    model= AppliedJobs
    template= 'admin/applied_student_list.html'

    def get(self, request):
        job_id= request.GET.get('job_id')
        
        if 'filter' in request.GET.dict():
            applied_job_list= self.model.objects.filter(job__id=job_id, status= request.GET.get('filter'))
        else:
            applied_job_list= self.model.objects.filter(job__id=job_id)


        context={
            "applied_job_list": applied_job_list,
            'status_list': [data[0] for data in STATUS_S],
            'job_id':job_id
        }

        
        return render(request, self.template, context)

class ChageAppliedJobStatus(View):
    model= AppliedJobs

    def get(self, request):
        redirect_to = request.META.get('HTTP_REFERER')
        print(redirect_to)
        aj_id= request.GET.get('aj_id')
        status= request.GET.get('status')
        
        applied_job= self.model.objects.get(id=aj_id)
        applied_job.status= status
        applied_job.save()
        messages.success(request, "Status is changed.....")
        return redirect(redirect_to)
