from django.contrib import admin

from .models import User,Jobs,AppliedJobs, StudentDetails

admin.site.register(User)
admin.site.register( Jobs)
admin.site.register(AppliedJobs)
admin.site.register(StudentDetails)
