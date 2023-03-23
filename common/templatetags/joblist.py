from django import template
register = template.Library()
from ..models import AppliedJobs, Jobs, StudentDetails

@register.simple_tag
def check_apply(job, user):
    apply_result= False
    status= 'NA'
    data={}
    try:
        job= AppliedJobs.objects.get(job=job, user=user)
        apply_result= True
        status= job.status
        data['apply_result']=apply_result
        data['status']=status
    
    except:
        data['apply_result']=apply_result
        data['status']=status

    return data

@register.filter
def check_apply_filter(data_dict, filter):
    return data_dict[filter]



@register.simple_tag
def apply_count(user):
    job_list= AppliedJobs.objects.filter(user=user)
    in_process = job_list.filter(status='in_process').count()
    selected = job_list.filter(status='selected').count()
    data={
        'job_list':job_list.count(),
        'in_process':in_process,
        'selected':selected
    }
    return data

@register.filter
def apply_count_filter(data_dict, filter):
    return data_dict[filter]

@register.simple_tag
def all_jobs_count():
    job_list= Jobs.objects.all().count()
    return job_list

@register.simple_tag
def get_profile(user):
    print(user)
    try:
        profile= StudentDetails.objects.get(user=user)
        return profile
    except:
        return None
    