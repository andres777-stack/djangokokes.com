from django.contrib import admin
from .models import *

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['title', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created', 'updated') 
        return () 

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    model = Applicant
    list_display = ['first_name', 'last_name', 'job', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created', 'updated') 
        return () 
# Register your models here.
