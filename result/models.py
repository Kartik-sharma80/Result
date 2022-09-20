from django.db import models

# Create your models here.
class Student(models.Model):
    exam_name = models.CharField(null=True, max_length=100)
    exam_month = models.CharField(null=True, max_length=20)
    year = models.CharField(null=True, max_length=20)
    semester = models.CharField(null=True, max_length=20, unique=True)
    roll_no = models.CharField(max_length=20, primary_key=True, null=False)
    name = models.CharField(null=True, max_length=20)
    father_name = models.CharField(null=True, max_length=20)
    mother_name = models.CharField(null=True, max_length=20)
    category = models.CharField(null=True, max_length=30)
    enroll_no = models.CharField(null=True, max_length=50)
    dob = models.DateField(null=True)
    sub1_name = models.CharField(null=True, max_length=70)
    sub2_name = models.CharField(null=True, max_length=70)
    sub3_name = models.CharField(null=True, max_length=70)
    sub4_name = models.CharField(null=True, max_length=70)
    sub5_name = models.CharField(null=True, max_length=70)
    sub6_name = models.CharField(null=True, max_length=70)
    sub7_name = models.CharField(null=True, max_length=70)
    sub1_marks = models.IntegerField(null=True)
    sub2_marks = models.IntegerField(null=True)
    sub3_marks = models.IntegerField(null=True)
    sub4_marks = models.IntegerField(null=True)
    sub5_marks = models.IntegerField(null=True)
    sub6_marks = models.IntegerField(null=True)
    sub7_marks = models.IntegerField(null=True)
    result = models.CharField(null=True, max_length=50)
    result_date = models.DateField(null=True)

    def __str__(self):
        return self.roll_no
