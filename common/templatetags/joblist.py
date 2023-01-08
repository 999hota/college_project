from django import template
register = template.Library()
from ..models import AppliedJobs 

@register.simple_tag
def check_apply(job, user):
    if AppliedJobs.objects.filter(job=job, user=user).exists()==False:
        print("Faslse")
        return False
    else:
        print("rue")
        return True


@register.simple_tag
def apply_count(user):
    count=AppliedJobs.objects.filter(user=user).count()
    return count