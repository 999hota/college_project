
from django.urls import path


from .views import *
from .student import student

app_name="common"
urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name="logout"),
    path("otp_verification", OtpVerification.as_view(), name="otp_verification"),
    path('student_register', student.StudentResgister.as_view(), name='student_register'),
    path('std_dash', StudentDashboard.as_view(), name='std_dash'),
    path('job_detail/<str:job_id>', JobDetails.as_view(), name='job_details'),
    path('apply_job/<str:job_id>', JobApply.as_view(), name="apply_job"),

    path('admin_dash',AdminDashboard.as_view(), name="admin_dash"),
    path('create_job', CreateJob.as_view(), name='create_job'),
    path('applied_student_list', GetAppliedStudentList.as_view(), name='applied_student_list'),
    path('chage_applied_job_status', ChageAppliedJobStatus.as_view(), name='chage_applied_job_status'),
]
