from django.contrib import admin
from admissions.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'bloodGroup', 'age', 'contact']


# Register your models here.
admin.site.register(Student, StudentAdmin)
