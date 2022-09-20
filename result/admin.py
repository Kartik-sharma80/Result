from django.contrib import admin
from result.models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
 list_display = ['roll_no', 'name', 'father_name', 'semester', 'year']
