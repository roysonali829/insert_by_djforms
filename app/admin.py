from django.contrib import admin

from app.models import *

# Register your models here.


class CustomStudent(admin.ModelAdmin):
    list_display = ['Sname','Sid','Semail']
    list_display_links = ['Sid']
    list_editable = ('Sname',)
    search_fields = ['Sname']
    list_filter = ['Semail']

admin.site.register(Student,CustomStudent)