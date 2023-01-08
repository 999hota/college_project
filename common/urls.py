
from django.urls import path


from .views import *

app_name="common"
urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('std_dash', StudentDashboard.as_view(), name='std_dash'),
    path('job_detail/<str:job_id>', JobDetails.as_view(), name='job_details'),
    path('apply_job/<str:job_id>', JobApply.as_view(), name="apply_job")
]
